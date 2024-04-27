"""Code runner...take lines of code, interpret and execute them"""
import registers, labels
from files import Files


_instruction_pointer = 0


def get_instruction_pointer():
    return _instruction_pointer


def set_instruction_pointer(value):
    global _instruction_pointer

    _instruction_pointer = value


def increment_instruction_pointer():
    global _instruction_pointer

    _instruction_pointer += 1


def setup_labels(code):
    """Make a pass through code to find all MARK statements."""
    for instruction_ptr, (instruction, *args) in enumerate(code):
        if instruction == 'MARK':
            labels.make_label(args[0], instruction_ptr)


def print_state(statement=None):
    if statement:
        print(f'{" ".join(statement):<12}', end=' ... ') # print line of code
    registers.print_registers()


# Here we implement the EXA instructions
# Normally we wouldn't use all caps for functions names,
# but I like the consistency...

def COPY(value, register_name):
    """Copy the value of the first operand into the second operand"""
    value = get_register_contents_or_value(value)
    registers.set_register(register_name, value)


def ADDI(value1, value2, register_name):
    """Add the value of the first operand to the value of the second
    operand and store the result in the third operand"""
    registers.set_register(register_name,
                 get_register_contents_or_value(value1) +
                 get_register_contents_or_value(value2)
    )


def SUBI(value1, value2, register_name):
    """Same as ADDI, for substraction"""
    registers.set_register(register_name,
                 get_register_contents_or_value(value1) -
                 get_register_contents_or_value(value2)
    )


def MULI(value1, value2, register_name):
    """Same as ADDI, for multiplication"""
    registers.set_register(register_name,
                 get_register_contents_or_value(value1) *
                 get_register_contents_or_value(value2)
    )


def DIVI(value1, value2, register_name):
    """Same as ADDI, for integral division"""
    registers.set_register(register_name,
                 get_register_contents_or_value(value1) //
                 get_register_contents_or_value(value2)
    )

def MODI(value1, value2, register_name):
    """Same as ADDI, for modulo"""
    registers.set_register(register_name,
                 get_register_contents_or_value(value1) %
                 get_register_contents_or_value(value2)
    )


def TEST(operand1, oper=None, operand2=None):
    """Handle TEST =, <, and >"""

    import operator

    # we can leverage Python's operator module to perform
    # the <, >, and =(=) operations...
    operator_mapper = {
        '=': operator.eq,
        '<': operator.lt,
        '>': operator.gt,
    }

    if operand1 == "EOF":
        result = Files.is_current_file_at_eof()
        print(f'TEST EOF = {result}')
    else:
        result = operator_mapper[oper](
            get_register_contents_or_value(operand1),
            get_register_contents_or_value(operand2)
        )
        print(f'TEST {operand1} {oper} {operand2} = {result}')
    registers.set_register('T', int(result)) # convert Bool to into


def TJMP(mark):
    if registers.get_register('T'):
        set_instruction_pointer(labels.get_label(mark))


def FJMP(mark):
    if not registers.get_register('T'):
        set_instruction_pointer(labels.get_label(mark))


def JUMP(mark):
    set_instruction_pointer(labels.get_label(mark))

# Map function names to functions which implement them
# Must be defined *after* the functions!

func_mapper = {
    "COPY": COPY,
    "ADDI": ADDI,
    "SUBI": SUBI,
    "MULI": MULI,
    "DIVI": DIVI,
    "MODI": MODI,
    "TEST": TEST,
    "MARK": lambda x: None, # nothing to do since labels already stored
    "TJMP": TJMP,
    "FJMP": FJMP,
    "JUMP": JUMP,
    "GRAB": Files.GRAB,
    "DROP": Files.DROP,
    "SEEK": Files.SEEK,
    "VOID": Files.VOID,
}

def run_statement(statement):
    """Run a statement/line of code"""

    # break it into instruction (e.g,. COPY, ADDI, etc.)
    # followed by arguments
    instruction, args = statement[0], statement[1:]
    if instruction in func_mapper: # valid instruction?
        # call the appropriate function and pass the args
        func_mapper[instruction](*args)
    else:
        raise Exception(f'Illegal instruction: {instruction}')


def run_code(code):
    while code[get_instruction_pointer()][0] != 'END':
        print_state(code[get_instruction_pointer()])
        run_statement(code[get_instruction_pointer()])
        increment_instruction_pointer()

    Files.print_final_value_of_files()

# Since all operations take a register OR a number as the
# first argument, it would be good to have a function which
# determines which it is, and validates it.

def get_register_contents_or_value(value):
    """Return a value, either a number or the contents
    of a register.
    """
    if registers.is_valid_register_name(value):
        return registers.get_register(value)

    # otherwise we expect it to be a number -9999..9999
    try:
        value = int(value) # try to int-ify
    except ValueError:
        raise Exception('Non-integer found')
    else:
        return value

"""Code runner...take lines of code, interpret and execute them"""
from registers import set_register, get_register, is_valid_register_name
from registers import print_registers
from exceptions import IllegalInstructionError

def print_state(statement=None):
    if statement:
        print(f'{" ".join(statement):<12}', end=' ... ') # print line of code
    print_registers()


# Here we implement the EXA instructions
# Normally we wouldn't use all caps for functions names,
# but I like the consistency...

def COPY(value, register_name):
    """Copy the value of the first operand into the second operand"""
    value = get_register_contents_or_value(value)
    set_register(register_name, value)


def ADDI(value1, value2, register_name):
    """Add the value of the first operand to the value of the second
    operand and store the result in the third operand"""
    set_register(register_name,
                 get_register_contents_or_value(value1) +
                 get_register_contents_or_value(value2)
    )


def SUBI(value1, value2, register_name):
    """Same as ADDI, for substraction"""
    set_register(register_name,
                 get_register_contents_or_value(value1) -
                 get_register_contents_or_value(value2)
    )


def MULI(value1, value2, register_name):
    """Same as ADDI, for multiplication"""
    set_register(register_name,
                 get_register_contents_or_value(value1) *
                 get_register_contents_or_value(value2)
    )


def DIVI(value1, value2, register_name):
    """Same as ADDI, for integral division"""
    set_register(register_name,
                 get_register_contents_or_value(value1) //
                 get_register_contents_or_value(value2)
    )

def MODI(value1, value2, register_name):
    """Same as ADDI, for modulo"""
    set_register(register_name,
                 get_register_contents_or_value(value1) %
                 get_register_contents_or_value(value2)
    )


def TEST(operand1, oper, operand2):
    """Handle TEST =, <, and >"""

    import operator

    # we can leverage Python's operator module to perform
    # the <, >, and =(=) operations...
    operator_mapper = {
        '=': operator.eq,
        '<': operator.lt,
        '>': operator.gt,
    }

    result = operator_mapper[oper](
        get_register_contents_or_value(operand1),
        get_register_contents_or_value(operand2)
    )

    set_register('T', int(result)) # convert Bool to into


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
        raise IllegalInstructionError(instruction)


def run_code(code):
    for statement in code:
        run_statement(statement)
        print_state(statement)

# Since all operations take a register OR a number as the
# first argument, it would be good to have a function which
# determines which it is, and validates it.

def get_register_contents_or_value(value):
    """Return a value, either a number or the contents
    of a register.
    """
    if is_valid_register_name(value): # instruction specifies a registers
        return get_register(value)

    # otherwise we expect it to be a number -9999..9999
    try:
        value = int(value) # try to int-ify
    except ValueError:
        raise IllegalInstructionError
    else:
        return value

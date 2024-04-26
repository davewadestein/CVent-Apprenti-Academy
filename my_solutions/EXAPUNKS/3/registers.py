"""Registers live and breathe here..."""

# store the registers in a dict...we could make a class but
# at this point seems like overkill to me...
registers = {
    'X': 0,
    'T': 0,
}

# we should make functions to read and write registers,
# rather than reading/writing to them directly...

def get_register(name):
    return registers[name]


def set_register(name, value):
    registers[name] = value


def is_valid_register_name(name):
    return name in registers


def print_registers():
    for name in registers:
        print(f'{name} = {registers[name]}', end='  ')
    print()

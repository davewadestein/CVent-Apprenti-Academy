"""Registers live and breathe here..."""
from files import Files

# store the registers in a dict...we could make a class but
# at this point seems like overkill to me...
registers = {
    'X': 0,
    'T': 0,
    'F': None,
}

# we should make functions to read and write registers,
# rather than reading/writing to them directly...

def get_register(name):
    validate_register_name(name)
    if name == 'F': # read from 'file' instead of registers
        registers[name] = Files.read_value_from_file()
    return registers[name]


def set_register(name, value):
    validate_register_name(name)
    if name == 'F':
        Files.write_value_to_file(value)
    registers[name] = value


def is_valid_register_name(value):
    return value in registers


def validate_register_name(name):
    if name == 'F' and not Files.file_is_open():
        raise Exception("Invalid F register access: File not open!")
    if name not in registers:
        raise Exception(f"Invalid register name: {name}")


def print_registers():
    for name in registers:
        print(f'{name} = {registers[name]}', end='  ')
    print()

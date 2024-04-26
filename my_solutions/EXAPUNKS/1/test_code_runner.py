from code_runner import * # BAD except for testing
from registers import *
from exceptions import *
import pytest

def test_run_unknown_statement():
    with pytest.raises(IllegalInstructionError):
        run_statement('FOO')


def test_run_statement():
    run_statement('COPY 5 X'.split())
    assert get_register('X') == 5


def test_run_code():
    run_code(['COPY 5 X'.split(), 'ADDI X 1 X'.split()])
    assert get_register('X') == 6


def test_get_value_register():
    registers['X'] = 100
    assert get_register_contents_or_value('X') == 100


def test_get_value_constant():
    assert get_register_contents_or_value('100') == 100


def test_COPY():
    COPY(1, 'X')
    assert registers['X'] == 1
    COPY('X', 'T')
    assert registers['T'] == 1


def test_ADDI():
    ADDI(1, 1, 'X')
    assert registers['X'] == 2
    ADDI('X', 1, 'X')
    assert registers['X'] == 3


def test_SUBI():
    SUBI(1, 1, 'X')
    assert registers['X'] == 0
    SUBI('X', 1, 'X')
    assert registers['X'] == -1


def test_MULI():
    MULI(2, 2, 'X')
    assert registers['X'] == 4
    MULI('X', 10, 'X')
    assert registers['X'] == 40


def test_DIVI():
    DIVI(8, 2, 'X')
    assert registers['X'] == 4
    DIVI('X', 2, 'X')
    assert registers['X'] == 2


def test_MODI():
    MODI(19, 5, 'X')
    assert registers['X'] == 4
    MODI('X', 2, 'X')
    assert registers['X'] == 0

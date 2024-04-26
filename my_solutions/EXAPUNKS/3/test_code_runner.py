from code_runner import * # BAD except for testing
import code_runner # for "private" vars
from registers import *
from exceptions import *
from labels import *
import pytest


def test_run_unknown_statement():
    with pytest.raises(Exception):
        run_statement('FOO')


def test_run_statement():
    run_statement('COPY 5 X'.split())
    assert get_register('X') == 5


def test_run_code():
    run_code(['COPY 5 X'.split(), 'ADDI X 1 X'.split(), ['END']])
    assert get_register('X') == 6


def test_instruction_pointer():
    set_instruction_pointer(1)
    assert code_runner._instruction_pointer == 1
    code_runner._instruction_pointer = 2
    assert get_instruction_pointer() == 2


def test_setup_labels():
    labels = {} # clear all setup_labels
    setup_labels(['MARK ZERO'.split()])
    assert get_label('ZERO') == 0


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


def test_TEST_eq():
    TEST(1, '=', 1)
    assert get_register('T') == 1
    TEST(1, '=', 2)
    assert get_register('T') == 0
    set_register('X', 0)
    TEST('X', '=', 'T')
    assert get_register('T') == 1
    ADDI('X', 2, 'X')
    TEST('X', '=', 'T')
    assert get_register('T') == 0


def test_TJMP():
    set_instruction_pointer(0)
    make_label('TRUE', 1)
    TEST(1, '=', 1)
    TJMP('TRUE')
    assert get_instruction_pointer() == 1


def test_FJMP():
    set_instruction_pointer(0)
    make_label('FALSE', 1)
    TEST(1, '=', 2)
    FJMP('FALSE')
    assert get_instruction_pointer() == 1


def test_JUMP():
    set_instruction_pointer(0)
    make_label('GOTO', 1)
    JUMP('GOTO')
    assert get_instruction_pointer() == 1

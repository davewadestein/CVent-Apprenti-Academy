from registers import * # BAD, except when testing
import pytest


def test_read_register():
    # let's put something into it manually,
    # then check we can see it w/our function
    registers['X'] = 123
    assert get_register('X') == 123


def test_read_register_invalid():
    with pytest.raises(Exception):
        get_register('nope!')


def test_write_register():
    # use the function to write, then check
    # manually if it worked...
    set_register('T', 123)
    assert registers['T'] == 123


def test_is_valid_register_name():
    assert is_valid_register_name('X')
    assert not is_valid_register_name('nope!')
    

def test_validate_register_name():
    validate_register_name('X') # should NOT throw an exception
    with pytest.raises(Exception):
        validate_register_name('nope!')

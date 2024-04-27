from labels import * # BAD but OK for testing
import pytest

def test_make_label():
    make_label('MAKE', 1)
    assert labels['MAKE'] == 1


def test_make_dupe_label():
    make_label('DUPE', 2)
    with pytest.raises(Exception):
        make_label('DUPE', 2)


def test_get_label():
    make_label('GET', 1)
    assert get_label('GET') == 1


def test_ensure_valid_label():
    make_label('VALID', 1)
    assert ensure_valid_label('VALID')


def test_ensure_valid_label_exception():
    with pytest.raises(Exception):
        assert ensure_valid_label('NOPE')


    

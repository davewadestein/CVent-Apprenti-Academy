from files import Files
from code_runner import *
from registers import *
from config import MAX_NUM
import pytest


def test_GRAB_exception():
    with pytest.raises(Exception):
        Files.GRAB("non-existent file")


def test_GRAB_already_open():
    Files.current_file['name'] = None
    Files.files['GRABFILE'] = []
    Files.GRAB("GRABFILE")
    with pytest.raises(Exception):
        Files.GRAB("GRABFILE")


def test_GRAB():
    Files.current_file['name'] = None
    Files.files['GRABFILE'] = []
    Files.GRAB("GRABFILE")
    assert Files.current_file['name'] == "GRABFILE"


def test_DROP():
    Files.DROP()
    Files.files['DROPFILE'] = []
    Files.GRAB("GRABFILE")
    Files.DROP()
    assert Files.current_file['name'] == None


def test_SEEK():
    Files.current_file['name'] = None
    Files.files['SEEKFILE'] = [0, 0, 0, 0]
    Files.GRAB("SEEKFILE")
    Files.SEEK(2) # move ahead 2 slots
    assert Files.current_file['cursor'] == 2


def test_SEEK_min():
    Files.current_file['name'] = None
    Files.files['MINFILE'] = [0] * 10
    Files.GRAB("MINFILE")
    Files.SEEK(-MAX_NUM)
    assert Files.current_file['cursor'] == 0


def test_SEEK_max():
    Files.current_file['name'] = None
    Files.files['MAXFILE'] = [0] * 10
    Files.GRAB("MAXFILE")
    Files.SEEK(MAX_NUM)
    assert Files.is_current_file_at_eof()


def test_VOID():
    Files.current_file['name'] = None
    Files.files['VOIDFILE'] = [1, 2, 3, 4]
    Files.GRAB("VOIDFILE")
    Files.VOID()
    assert Files.files['VOIDFILE'] == [2, 3, 4]


def test_VOID_no_file_open():
    Files.current_file['name'] = None
    with pytest.raises(Exception):
        Files.VOID()


def test_VOID_file_at_eof():
    Files.current_file['name'] = None
    with pytest.raises(Exception):
        Files.VOID()


def test_file_is_open():
    Files.current_file['name'] = 'something'
    assert Files.file_is_open()


def test_read_value_from_file():
    Files.current_file['name'] = None
    Files.files['READVALFILE'] = [1]
    Files.GRAB('READVALFILE')
    assert Files.read_value_from_file() == 1 and \
                Files.current_file["cursor"] == 1


def test_TEST_EOF():
    Files.current_file['name'] = None
    Files.files['EOF'] = []
    Files.GRAB('EOF')
    TEST('EOF')
    assert get_register('T')

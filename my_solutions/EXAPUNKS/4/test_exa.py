import pytest
import pathlib
from exa import read_code

def test_read_code():
    # make a test file to read
    with open('testfile', 'w') as test_file:
        print('COPY 70 X', file=test_file)
    # now that we've created a file be sure
    # we can read from the file
    code = read_code('testfile')
    assert code == [['COPY', '70', 'X'], ['END']]
    pathlib.Path("testfile").unlink() # clean up by removing file


def test_read_code_file_not_exist():
    # attempting to read from a file that does not exit...
    # ...should raise a FileNotFoundError
    with pytest.raises(FileNotFoundError):
        read_code('somefilethatdoesnotexist')

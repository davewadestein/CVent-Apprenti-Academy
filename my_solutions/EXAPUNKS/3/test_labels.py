from labels import * # BAD but OK for testing

def test_make_label():
    make_label('LABEL', 1)
    assert labels['LABEL'] == 1

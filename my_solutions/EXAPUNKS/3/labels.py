"""Dicts are pretty versatile and we can use them to keep
track of labels (lines of code we've MARKed) just like we
used them to keep track of registers and their values.
"""
labels = {}

def make_label(label, position):
    labels[label] = position


def get_label(label):
    pass


def ensure_valid_label(label):
    pass


def print_labels():
    pass

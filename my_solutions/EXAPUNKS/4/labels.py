"""Dicts are pretty versatile and we can use them to keep
track of labels (lines of code we've MARKed) just like we
used them to keep track of registers and their values.
"""
labels = {}

def make_label(label, position):
    if label in labels:
        raise Exception(f'Duplicate label: {label}')
    labels[label] = position


def get_label(label):
    return labels[label]


def ensure_valid_label(label):
    if label not in labels:
        raise Exception(f'Invalid label: {label}')
    return True


def print_labels():
    print('\n'.join(labels.values()))

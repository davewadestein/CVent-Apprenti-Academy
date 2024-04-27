"""Part 1"""

import sys
import code_runner


# Any unknown instruction, register or invalid number should result in an exception thrown (stopping the program)
# Leading spaces (at the start of a line of code) should be ignored
# Blank lines should be ignored

def read_code(codefile):
    """Read EXA code from a file on disk"""

    with open(codefile) as file:
        # read each non-empty line into a list, stripping spaces
        # and discarding empty lines
        code = []
        for line in file.readlines():
            line = line.strip()
            if len(line) > 1: # skip blank lines
                if '#' in line:
                    line = line[:line.index('#')] # strip comments
                code.append(line.split())

    # add an end marker to make it easier to know when
    # we are at the end of the codefile
    code.append(['END'])
    return code


if len(sys.argv) == 1:
    print('Missing filename!')
else:
    code = read_code(sys.argv[1]) # need to check for no arg
    code_runner.setup_labels(code)
    code_runner.run_code(code)

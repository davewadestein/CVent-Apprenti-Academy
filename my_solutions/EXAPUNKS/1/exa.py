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
        code = [line.strip().split()
                    for line in file.readlines()
                        if line != '\n']
    return code

if len(sys.argv) == 1:
    print('Missing filename!')
else:
    code = read_code(sys.argv[1]) # need to check for no arg
    code_runner.run_code(code)

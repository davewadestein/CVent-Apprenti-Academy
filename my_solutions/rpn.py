"""RPN calculator."""
import operator
from collections import defaultdict
import stack

the_stack = stack.Stack() # we only need one–we could talk about "singleton pattern"

# This dict maps operators to the functions under the hood which perform those operations.
# We can use it as is, and just ensure the operator the user entered is in the dict...
operator_to_function_dict = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
   '**': operator.pow,
    '/': operator.truediv,
   '//': operator.floordiv,
    '%': operator.mod,
}

# Or we can use a defaultdict to avoid crashing, but once I did this I figured
# it was more trouble that it's worth in this case. But leaving it here as an
# example for you. Below we create a defaultdict that will return None if the
# key isn't in the dict. The second arg allows us to initialize the defaultdict
# with the values already in the dict above...
operator_to_function_mapper = defaultdict(lambda: None, operator_to_function_dict)

def to_num(string):
    """Try to convert string to int/float and return value if we can. Otherwise return None."""
    try:
        result = int(string)
    except ValueError:
        pass
    else:
        return result

    try:
        result = float(string)
    except ValueError:
        return None
    else:
        return result
    
def perform_calculation(operator):
    """Perform calculations on stack items. Consider adding unary operators
    (e.g., log). Rather than perform the calculation ourselves, we can lean
    on Python's operator moduland create a dict to look up operator and find
    appropriate function to call. See above.
    """
    if the_stack.size() < 2: # 1 for unary operator...
        print("Binary operators need two operands on the stack!")
        return None
        
    second = the_stack.pop()
    first = the_stack.pop()
    result = operator_to_function_mapper[operator](first, second)
    print(f'{first} {operator} {second} = {result}')
    return result

def rpn():
    while (response := input()): # get input until user hits return to stop
        # assume space-separated--we could work harder to deal with lack of spaces
        for thing in response.split():
            if thing == 'c': # clear
                the_stack.clear()
                break
            if value := to_num(thing): # is it a number
                the_stack.push(to_num(thing))
            elif thing in operator_to_function_dict:
                if result := perform_calculation(operator=thing):
                    the_stack.push(result)
                else: # error, so clear the stack
                    the_stack.clear() 
            else:
                print(f"Unknown operator: {thing}")
                the_stack.clear()

rpn()

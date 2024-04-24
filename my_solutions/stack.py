class Stack(list):
    """Stack class for RPN calculator.
    
    At the very least, we want a push() method to mirror the pop() method.

    We also override pop() to provide an appropriate (custom) exception when popping an empty stack
    and a few other helper methods.
    """

    class StackUnderFlowError(Exception):
        """Custom exception to indicate underflow."""

    def __init__(self, debug=False):
        """Create a stack. If debug is True, we'll print some debugging..."""
        self.debug = debug
        super().__init__() # finish init in the parent class
    
    def push(self, item):
        """Push an item on the stack."""
        if self.debug:
            print('push', item)
        self.append(item)

    def pop(self):
        """Pop an item from the stack. If empty, throw our custom exception."""
        if self.debug:
            print('pop', self.top())
        if self.size() > 0:
            return super().pop()
        raise self.StackUnderFlowError("Can't pop an empty stack!")

    def clear(self):
        """Clear the stack."""
        super().clear()
        
    def size(self):
        """Return number of items on the stack."""
        return len(self)

    def top(self):
        """Return top item without popping it."""
        if self.size() > 0:
            return self[-1]
        raise self.StackUnderFlowError("Can't see top of an empty stack!")

    def is_empty(self):
        """Return True if stack is empty."""
        return len(self) == 0

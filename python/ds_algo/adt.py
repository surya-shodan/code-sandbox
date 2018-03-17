class ADT:
    pass

class Stack:
    """Implements a stack in Python"""

    def __init__(self):
        """Constructor which initializes/sets the variables"""

        self.MAX_SIZE = 10000
        self.__stack = list()
        self.__top = 0

    def push(self, item):
        """Pushes an item at the end of the stack
        O(1) Time Complexity"""

        if self.__top == self.MAX_SIZE:
            raise Exception('Stack Overflow')
        self.__top += 1
        self.__stack.append(item)
        return self.__stack

    def get_stack(self):
        """Returns Stack contents
        """

        return self.__stack

    def size(self):
        """Returns current size
        """

        return self.__top

    def peek(self):
        """Returns the top element
        """

        return self.__stack[self.__top - 1]

    def pop(self):
        """Pops an item at the end of the stack
        O(1) Time Complexity"""

        if self.__top == 0:
            raise Exception('Stack Underflow')
        self.__top -= 1
        popped = self.__stack.pop()
        return popped

    def is_empty(self):
        """Returns True if stack is empty
        """

        return (self.__top == 0)

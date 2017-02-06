class Empty(Exception):
    """
    This is a custom error for stacks, queues, etc from chapter 6.
    """
    pass

class ArrayStack:
    """
    A Python implementation of a LIFO stack made from a Python list.
    """
    def __init__(self):
        """
        Create an empty stack.
        """
        self._data = []

    def __len__(self):
        """
        returns the number of elements.
        """
        return len(self._data)

    def is_empty(self):
        """
        Return True if the stack is empty.
        """
        return len(self._data) == 0

    def push(self, e):
        """
        Adds another element to the top of the stack.
        """
        self._data.append(e)

    def top(self):
        """
        Return the element at the top of a stack, but don't remove it.
        Raise exception if stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        """
        This returns the top element, and also removes it.
        Else, raise an error if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

def reverse_file(filename):
    """
    This function reverses the contents of a file (in place & line by line) by placing each line onto a stack, then removing it and writing the results to a file.
    """
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))       # Notice how we can specify the string to be stripped.
    original.close()

    # Now we overwrite the original file with the reversed contents..
    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()

if __name__ == '__main__':
    import random
    a = ArrayStack()
    print('LENGTH: ', len(a))
    if a.is_empty():
        print('PASS: is_empty')
    a.push(1)
    a.push(2)
    a.push(3)
    print('LENGTH: ', len(a))
    for i in range(len(a)):
        print("Removed ", i, a.pop())
        print('LENGTH: ', len(a))
    print("Finished!")

    f = 'file.test'
    reverse_file(f)

class Empty(Exception):
    """
    Custom error.
    """

class ArrayStack:
    """
    LIFO stack using a list as storage.
    """
    def __init__(self):
        """
        Create an empty stack.
        """
        self._data = []

    def __len__(self):
        """
        Return length.
        """
        return len(self._data)

    def is_empty(self):
        """
        Return True if empty.
        """
        return len(self._data) == 0

    def push(self, e):
        """
        Add element e to the top of stack.
        """
        self._data.append(e)

    def top(self):
        """
        Return, but do not remove, the element at the top of the stack.
        
        Else raise Exception.
        """
	if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        """
        Return, and remove, the element from the top of the stack.

        Else, raise error.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()
            
## __len__, push, top, pop
#if __name__ == '__main__':
#    arraystack = ArrayStack()
#    print('length equals: ', len(arraystack))
#    arraystack.push('first')
#    print('length equals: ', len(arraystack))
#    arraystack.push('second')
#    print('length equals: ', len(arraystack))
#    arraystack.push('third')
#    print('length equals: ', len(arraystack))
#    print('this is the whole array: ', arraystack._data)
#    print('the item at the top of the stack is ', arraystack.top())
#    try:
#        while arraystack.top():
#            print(arraystack.pop())
#            print('new length is ', len(arraystack))
#    except Exception as e:
#        pass

def reverse_file(filename):
    """
    Reverse the contents of a file's text, line by line.

    From p. 235
    """
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()

    # Now use stack to reverse contents, and write to file
    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()

if __name__ == '__main__':
    content = [
    'first line\n',
    'second line\n',
    'third line\n',
    ]
    testfile = '/home/justin/tmp/reversefile.test'
    with open(testfile, 'w') as f:
        for line in content:
            f.write(line)

    print('the contents of the original file is:')
    for line in open(testfile).readlines():
        print(line)
    print('now we will reverse the contents of the file...')
    print('this is the original contents of the file: ')
    with open(testfile) as f:
        for line in f.readlines():
            print(line)
    reverse_file(testfile)
    print('this is after calling reverse_file()')
    with open(testfile) as f:
        for line in f.readlines():
            print(line)



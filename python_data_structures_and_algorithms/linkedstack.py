class Empty(Exception):
    """
    This error is raised when an attempt is made to access an element from an empty list.
    """

class LinkedStack:
    """
    LIFO Stack implementation using a singly linked list for storage.

    This is from page 263 of the book.
    """
    #------------ nested _Node class -----------------
    class _Node:
        """
        This is a convenient, lightweight nonpublic class for storing a singly linked node.
        The '__slots__'  statically defines the instance attributes.
        """
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    #------------ stack methods----------------
    def __init__(self):
        """
        initialize an empty stack.
        """
        self._head = None           # this is the head node
        self._size = 0              # this keeps a count of the number of stack elements
    
    def __len__(self):
        """
        this returns the number of elements in the stack.
        """
        return self._size

    def is_empty(self):
        """
        True if the stack is empty.
        """
        return self._size == 0

    def push(self, e):
        """
        Add element to the top of the stack.
        """
        self._head = self._Node(e, self._head)          # this creates and links a new node
        self._size += 1

    def top(self):
        """
        Return, but do not remove, the element at the top of the stack.
        
        Will Taise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element          # top of stack is at head of list

    def pop(self):
        """
        Remove and return the element from the top of the stack (ie: LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next           # bypass the former to node
        self._size -= 1
        return answer

# methods: len, is_empty, push, top, pop
if __name__ == '__main__':
    ls = LinkedStack()
    print('the len of ls is:    ', len(ls))
    print('is ls empty?     ', ls.is_empty())
    l = [
    'first',
    'second',
    'third',
    ]
    for item in l:
        ls.push(item)
        print('the len of ls is:    ', len(ls))
        print('the first element is:    ', ls.top())
    print('is ls empty?     ', ls.is_empty())
    while len(ls) != 0:
        print('popping top element:     ', ls.pop())

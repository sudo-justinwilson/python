class LinkedStack:
    """
    LIFO Stack implementation using a singly linked list for storage.
    """
    # ----------------- nested class:
    class _Node:
        """
        Lightweight, nonpublic class for storing a singly linked node.
        """
        __slots__ = '_element', '_next'         # statically define instance attrs

        def __init__(self, element, next):
            # initialize node with element and pointer to next node:
            self._element = element
            self._next = next

    # -------------------------- stack methods:
    def __init__(self):
        """
        Create an empty stack.
        """
        self._head = None
        self._size = 0

    def __len__(self):
        """
        Return the number of elements in the stack.
        """
        return self._size

    def is_empty(self):
        """
        Return True if the stack is empty.
        """
        return self._size == 0

    def push(self, e):
        """
        Add element e to the top of the stack.
        """
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        """
        Return, but do not remove the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def pop(self):
        """
        Remove and return the element from the top of the stack (LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

if __name__ == '__main__':
    l = LinkedStack()
    l.push('first')
    print(len(l))
    l.push('second')
    l.push('third')
    l.push('fourth')
    print(len(l))
    print(l.top())
    while len(l):
        print(l.pop())
        print(len(l))
    print('Is the stack empty? ', l.is_empty())

class LinkedQueue:
    """
    LIFO queue using a singly linked list.
    """
    # -------- nested class:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    # --- start stack methods:
    def __init__(self):
        """
        Create an empty stack.
        """
        self._head = None
        self._size = 0

    def __len__(self):
        """
        Return number of elements in stack.
        """
        return self._size

    def is_empty(self):
        """
        Return True if empty.
        """
        return self._size == 0

    def push(self, e):
        """
        Add e to the top of the stack.
        """
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        """
        Return, but do not remove, the top element.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def pop(self):
        """
        Remove and return the top element.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

if __name__ == '__main__':
    l = LinkedQueue()
    l.push('first')
    print(len(l))
    print(l.pop())
    print(len(l))
    print('Linked list is empty: ', l.is_empty())
    l.push('second')
    print(len(l))
    print('Linked list is empty: ', l.is_empty())
    print(l.pop())
    print(len(l))

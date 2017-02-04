class CircularQueue:
    """
    Queue implementation using circularly linked storage.
    """
    # -------- nested class:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """
        Create an empty queue.
        """
        self._tail = None
        self._size = 0

    def __len__(self):
        """
        Return the number of elements in list.
        """
        return self._size

    def is_empty(self):
        """
        Return True if the qyeye is empty.
        """
        return self._size == 0

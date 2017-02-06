class ArrayQueue:
    """
    FIFO queue using python list for storage.
    """
    DEFAULT_CAPACITY = 10       # size of queue before it expands

    def __init__(self):
        """
        Create an empty list.
        """
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """
        Return the size of the queue.
        """
        return self._size

    def is_empty(self):
        """
        Return True if the queue is empty.
        """
        return self._size == 0

    def first(self):
        """
        Return, but do not remove, the first element.

        Else, raise Exception.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """
        Remove and return the first element (FIFO).

        else, raise Exception.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None      # help with garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """
        Add an element to the back of the queue.
        """
        if self._size == len(self._data):
            self._resize(2 * len(self._data))   # double the size of the array
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):      # assuming cap >= len(self)
        """Resize to a new list of capacity >= eln(self).
        """
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)        # use old size as modulus
        self._front = 0

# methods: len, is_empty, first, dequeue, enqueue, _resize
if __name__ == '__main__':
    aq = ArrayQueue()
    print('is aq empty?     ', aq.is_empty())
    print('the len of aq is:    ', len(aq))
    print('the length of the underlying list (self._data) is:   ', len(aq._data))
    l = [
    'first',
    'second',
    'third'
    'fourth',
    'fifth',
    'sixth',
    'seventh',
    'eighth',
    'ninth',
    'tenth',
    'eleventh',
    'twelveth',
    'thirteenth',
    ]
    for element in l:
        print('now putting ', element, ' in queue')
        aq.enqueue(element)
        print('the len of aq is:    ', len(aq))
        print('the length of the underlying list (self._data) is:   ', len(aq._data))
    print('the first element of aq is: ', aq.first())
    print('is aq empty?     ', aq.is_empty())
    while len(aq) != 0:
        print('dequeuing:   ', aq.dequeue())
        print('the len of aq is:    ', len(aq))
        print('the length of the underlying list (self._data) is:   ', len(aq._data))


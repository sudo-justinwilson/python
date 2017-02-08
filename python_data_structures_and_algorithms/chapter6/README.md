# Stacks, Queues and Dequeues
Stacks are a simple data type, which are ubiquitous throughout computers. They are also known as LIFO (last in, first out), just like a stack of dishes.

# Stacks (LIFO)

## The Stack abstract data type:
    - The stack ADT contains few methods:
    -- push     push an element onto the top of the stack.
    -- pop      remove, and return the element at the top of the stack.
    - These are additional methods commonly found with stacks:
    -- top      return, but do not return, the element at the top of the stack.
    -- is_empty()   True if the stack is empty.
    -- len      returns the number of elements in a stack.

## The Adapter pattern:
The adapter pattern is when we take an existing class, and implement to suit our needs, with a slighlty different interface and methods.
An example of an adapter pattern is taking the Python "List" class, hiding it behind our code, and presenting new methods so that it behaves as a Stack.

## Implementing an ArrayStack class, using a Python list as the backend storage:
In this code example, we define a class with a "Stack" interface, but behind the scenes, we are really using a Python list. As mentioned above, this is an example of an "Adapter Pattern", and it is a classic example of re-using code with OOP.
We just have to provide the methods for a Stack interface:
    - __init__()
        def __init__(self):
            """
            This creates an empty list for us to store the Stack elements.
            Note that _data is a non-public attribute, as it should not be invoked directly by the user.
            """
            self._data = []
    - push()
        def push(self, e):
            """
            This uses the append List method, which has the same effect as pushing an element onto a stack.
            """
            self.append(e)
    - pop()
        def pop(self):
            """
            This uses the pop() List method, else raise exception.
            """
            if self.is_empty():
                raise Empty('Stack is empty')
            return self._data.pop()
    - top()
        def top(self):
            """
            Return, but do not remove, the top element, else raise Exception.
            """
            if self.is_empty():
                raise Empty('Stack is empty')
            return self._data[-1]
    - is_empty()
    - __len__()
        def __len__(self):
            """
            This one is easy... just return the length of the internal list.
            """
            return len(self._data)

## Reversing the contents of a file, using Stacks:
If you picture a stack as a literal stack of plates, if we were to place dishes one by one onto a stack, and then remove them one by one, the stack would naturally be in the reversed order. We can use the same concept to reverse the order of any stack's elements.

## Using stacks to match delimiters:
The code example in section 6.1.4 shows us how we can ensure that delimiters are properly paired, (IE: if there is an opening bracket in some code "(", there obviously has to be a closing bracket ")".
In this example, we do this by iterating over each char in a string, and if that char is an opening delimiter, we then push it onto a Stack. As we continue looping over each character, if we encounter a closing delimiter, if there is no matching opening delimiter, it's obviously an error, but if there is a matching opening delimiter on the Stack, we pop it, until there are either no more chars, and the stack is empty, which would return True, else there are unmatched delimiters, which would return False indicating that they do not match.
I would imagine that this would be similar behaviour to how VIM and other IDEs would do it...

## Matching HTML tags using Stacks:
On p.238, the example shows us how to ensure that the HTML tags are properly opened, and closed:
1. We first create a stack, and look for the first instance of a "<", and assign the index of the char, in the string (which is an immutable array of chars) to the letter 'j'.
2. We then look for a ">", starting from position 'j+1', if there is no ">", the string.find() method will return -1, which means that the tags are not matched.
3. If we do find the matching ">", we assign it to 'k' and extract the tag, with a sub-slice (tag = raw[j+1:k]), and if the HTML tag does not start with a "/" (which is for closing HTML tags), we push the tag onto the Stack. 
4. If the tag does start with a "/", we compare it to the element that is popped from the stack, which should be either an opening tag that does not start with "/", or we know it's an unmatched tag, and return False.
4. We then continue iterating over the chars tarting from the char after the last tag we found, until we either find another "<", which we then go back to step (3), or we don't find any. If the stack is empty (because each time we find a tag, we push it onto the stack, and pop it once we found the closing tag that starts with "/"..) we return True (tags are matched). Otherwise if there is an element on the stack, it is unmatched and we return False.

# Queues (FIFO)

Queues are just what it sounds like. Last In First Out..

## Queue ADT:
The queue abstract data type could be implemented using a List (using pop(0) to remove the front element, and append(e) to add one) but would be inefficient, as if we use pop(:-1) to remove an element that is not at the back, each element gets looped over to shift left, and runs in OMEGA(n) time.
The most efficient way is to use a "Circular" list, where we maintain an index of the element which is logically at the font, but can move.
We basically keep an index of the front and rear elements, so when we want to "enqueue" an element to the back of the queue, we can just put it after L.index(last), and vise-versa with index(first).

The queue can also increase it's length dynamically if required.

### ArrayQueue:
    - EG: ArrayQueue
    L = [a=self._first, b, c]
    len(L) == 3
    If we dequeue the first element, the next element becomes self._first:
    L = [a=None, b=self._first, c]
    len(L) == 3 (--1)
    if L runs out of capacity:
    (len(L) * 2) * [None]
    If we add 2 more elements to the queue:
    L.enqueue(e, f)
    L = [None, b=self._first, c, e, f, None]
    It could eventually wrap around like:
    L = [c, e, f, None, None, b=self._first]
    It uses the following formula to calculate how to advance the index of self._front, even if it has to go around:
    self._front = (self._front % len(self._data)
    *self._data is the internal list

### Deque (Double Ended Queues)
Another type of queue is double-ended, meaning instead of just keeping the index of the front, we keep the index of the front and back.
It provides more functionality, as it allows elements to be added or removed from the front or back (not the middle!).

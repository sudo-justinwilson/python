# Stacks, Queues and Dequeues
Stacks are a simple data type, which are ubiquitous throughout computers. They are also known as LIFO (last in, first out), just like a stack of dishes.

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

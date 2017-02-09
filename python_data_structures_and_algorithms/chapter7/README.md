# Chapter 7 - Linked Lists
Linked lists are a data structure class, which have an attribute that points to the next element in the list. This allows linked lists to be flexible, as it can be distributed over anywhere where you can point to.
They are a flexible alternative to array based sequences.

**Linked Lists vs Dynamic Arrays:**
Linked lists can be more efficient with space,faster than dynamic arrays in some operations such as adding and removing inner elements.
Linked lists methods are not amortized either, which may be required in certain environments.

## Singly Linked Lists
A singly linked list is a struct that only knows which element is next (not before), so list traversal can only be one way:

    element1    element2     element3    element4    element5
       ^           ^            ^           ^           ^
       |           |            |           |           |
     head       node1         node2       node3       tail
     ____       ____          ____        _____       _____  
     next   ->   next  ->     next ->     next ->     next ->   None
     
        * Linked list nodes are comprised of the attributes:
            * element
            * next
    

Each singly linked list node consists of the following attributes:
    1. **object reference:**
    A reference to the actual object that the node represents. This could be anything such as a dict, list, string...
    2. **next reference:**
    This is a pointer to the next node in the linked list.
We need to remember head's position, so we know where the start of the list is. The tail reference is not strictly required, but without it, we would have to traverse the linked list whenever we wanted the position of the last element. It is also efficient to store the length of the list by adding/subtracting each time we add/remove a node.

The first node of the linked list is referred to as the _head_, and the last element is known as _tail_.
It is common for iterators to stop when they receive None. We also use this convention as the tail's next attribute points to None.

We can traverse the list by following each nodes _next_ reference, starting from the head, until we eventually reach the tail, which points to None. This is also known as "_link hopping_".

If you refer to the linked list representation above, a node's "element" attribute is a variable which can reference anything that can be assigned to a variable (anything!). The elements that the linked list point to, do not need to know they are members of a linked list.

### Inserting/removing elements with singly linked lists:
__Adding elements to the front:__
The flow for adding an element to the front of a singly linked list is as follows:

    1. We define a new node, whose _next_ element points to the incumbent head node.
    2. The __head__ reference gets reassigned to point to the new node.

__Appending elements to the end of a list:__
The procedure for adding a node after tail is:

    1. Define a new node, who's _next_ points to None.
    2. Reassign the linked list's _tail_ attribute, and the last node's _next_ element, so that it points to the new _tail_ node.

__Removing the first element of a singly linked list:__
Removing the head element is like adding an element, but in reverse. 
    1. Reassign linked list's _head_ element, so that it points to the next element (head.next)
    2. Remove references to the old head so that it is garbage collected.

With a singly linked list, there is no efficient way to remove the _tail_ node, as we need to reassign the _next_ pointer of the element before tail (second last). This is because singly linked lists only maintain a "_next_" attribute, but not "previous", making it "one-way", and hence the name.  

### Singly linked list implementation:
A singly linked list member is called a"__node_". We can represent a node with a non-public class, that is nested within the main linked list class definition:

```python
    class _Node:
        __slots__ = '_element', '_next'     # slots allow efficient memory use
        def __init__(self, next):
            self._element = element
          self._next = next
```

#### Linked List Attributes

So the only attributes we define are:

1. element
.Points to the actual object
2. next
  .Points to the node in the next position
3. head\n
  points to the first element
4. tail
    * points to the last element

#### Linked List Methods

The methods which we define are:

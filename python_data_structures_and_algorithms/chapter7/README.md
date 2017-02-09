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

Each time we add/remove an element, we increment/decrement self._size, so that we always know the length of the list.


The flow for adding an element to the front of a singly linked list is as follows:

1. We define a new node, whose _next_ attribute points to the incumbent head node.
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

A singly linked list member is called a "Node". We can represent a node with a non-public class, that is nested within the main linked list class definition:

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
    * Points to the actual object
2. next
    * Points to the node in the next position
3. head
    * points to the first element (not required for Stacks)
4. tail
    * points to the last element
5. size
    * the number of elements in the linked list

#### Linked List Methods

The methods that we define depend on how if we want to represent a LIFO, FIFO, etc..

As Stack operations (push, pop) are only performed at the top (_beginning_), there is no need for a _tail_ reference.

For a Queue, we need the ability to perform operations at the front (dequeue) and back (enqueue), so we define attributes to store their respective position.

Common methods include:

1. `__init__:`
    * This creates an empty linked list.
2. `is_empty:`
    * True if there are no elements, else False.

The methods should run with a worst case of _BIG-O(1)_ as it does not depend on the length of the linked list for both Stacks and Queues. This is due to the fact that we:

   * Increment/decrement the list length each time we add/remove and element.
   * Operations are performed on positions relative to known Node positions.
      * EG: 
        ```
        def push(self, e): self._head = self._Node(e, self._head), self._size += 1
        ```

#### Implementing Cirular Singly Linked Lists

Implementing circular linked lists is easier than doing so with _Arrays_, as we can point the _tail.next_ to the _head_, forming a natural circle.

The beginning and end of a linked list is totally abstract, which makes it easier to define where we want the list to start and end.

A circular linked list does not require a reference to _head_, as the _next_ element for _tail_ points to head (or None, if the list is empty), as opposed to a non-circular linked list, where tail.next points to None.

    ```head = tail._next()```

The only required attributes for a circular linked list are:

- tail
- size

We still abstract a node with the nested Node class, but use a unique method that rotates the list, which results in _tail_ advancing towards the front of the queue.

__Using a Linked List as a "Round-Robin" scheduler__

If there is a shared resource that is required by multiple programs, a scheduler can be used to ensure that the resource is shared equally. The Linux kernel uses this mechanism to allocate CPU time (though not in Python..).

We can implement a round-robin scheduler with a linked list as follows:

1. On a populated linked-list queue, we "dequeue" the first element, and store it in variable "e". "e" can point to a pid, web host, etc..
2. e is serviced.
3. e is then "enqueued" to the back of the queue, where it will wait in line to be serviced again.

We can also implement different algorithms that could be more "nice" to certain processes (think QOS).


## Doubly Linked Lists

A doubly linked list node has pointers to _next_ and _previous_.
This allows us to perform operations on elements before and after a Node.

We also define "dummy" nodes for the head and tail called "_sentinels_". These simplify the implementation as the head and tail are constant, and we always have a reference to the head and tail, even when the list is empty.

The sentinels do not point to elements, and are not included in the length of the list.

An empty doubly linked list is initialized with the _head_ pointing to _tail_, which creates an empty list.


### Adding/removing elements with doubly linked lists:

1. A new Node "N" is defined and shimmed into it's position by settting N's _next_ and _prev_ elements to the nodes before/after.
2. The preceeding node's next pointer, is set to point to N, and the prev pointer in the element after N is set to point at N.

The above operation can be performed anywhere in the list, as long as we know the preceding and following Nodes.

To insert at the front of the list, the preceding element would be the head sentinel, and vise-versa for the back.

To remove an element, we do the reverse of adding:

1. the nodes that are before and after are set to point at each other, bypassing the redundant node.
2. The redundant Node is set to point at None.

So in summary, a doubly linked list is differentiated by:

    1. the Node's extra attribute: __prev__
    2. the head and tail sentinels
    3. the ability to insert elements between existing Nodes

We can define a doubly-linked base ADT that has the basic methods for a doubly-linked list to function.
Sub-classes can inherit from this ADT and provide the user with an interface that suits their needs, whether they require a stack, queue, dequeue, etc..

p. 275

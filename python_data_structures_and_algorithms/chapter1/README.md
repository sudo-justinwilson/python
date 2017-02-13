# Python Basics

## 1.8: Iterators & Generators
__Iterators vs Iterables:__

_Iterators:_
An iterator is an object that cycles through each element of a collection by calling __next(iterable)__, until a _StopIteration_ is raised, which means there are no more elements.

_Iterables:_
An iterable is an object that can produce an iterator when the object is passed to __iter(object)__.
For example, a list is *not* an iterator and can not call next(list). But we can pass a list to iter(list), which would return an iterator that we can call next() on:

    l = [1,2,3,4]
    i = iter(l)
    next(i)
    1
    next(i)
    2
    ...

An iterator keeps its own reference to what index it's up to on the object. As an iterator just keeps an index to the collection, any updates to the collection will be reflected in the results when we call next().

This is what actually is happening in a forr loop. An iterator is produced from a sequence, and next(sequence) is called for each loop, until StopIteration is raised, which the for loop handles quietly.

__Generators:__
Generators are similar to iterators, but a function is performed and the result is returned by calling  __*yield()*__.

This lets us be efficient with memory as we only have to perform one operation at a time, instead of having to calculate all the values at once. 
Several yield() statements can be used with logic so that different results are yielded depending on the decision tree. 

# Chapter 5 - Array-Based Sequences

## How dynamic arrays are implemented:
    - First, we have an array of X pointers, where each element points to some object.
    - When the original array is exhausted, and does not have any more empty elements left to allocate, we create another array, which is usually double.
    The first X pointers of the new array, also consist of pointers that point to the same objects as the original array.
    - Once the new array references the same objects, we can safely remove the old array, or leave it for garbage collection.

## Using the built-in "__str__" method to print:
    - The __str__ method is the method that is actually called when we print an object. EG: print(obj) == obj.__str__(self)

*Up to p.212

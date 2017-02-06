# exercises from chapter 6

 R-6.1 What values are returned during the following series of stack operations, if executed upon an initially empty stack? push(5), push(3), pop(), push(2), push(8), pop(), pop(), push(9), push(1), pop(), push(7), push(6), pop(), pop(), push(4), pop(), pop().

    A) 5

R-6.2 Suppose an initially empty stack S has executed a total of 25 push operations, 12 top operations, and 10 pop operations, 3 of which raised Empty errors that were caught and ignored. What is the current size of S?

	A) 18?

R-6.3 Implement a function with signature transfer(S, T) that transfers all elements from stack S onto stack T, so that the element that starts at the top of S is the first to be inserted onto T, and the element at the bottom of S ends up at the top of T.

	A)
    def transfer(S, T):
        while len(l) > 0:
           s.append(l.pop())

-6.4 Give a recursive method for removing all the elements from a stack.

    A) 
	def remove(obj):
    if len(obj) > 0:
        obj.pop()
        return remove(obj)

R-6.5 Implement a function that reverses a list of elements by pushing them onto
a stack in one order, and writing them back to the list in reversed order.

	A)
	def revers(obj):
        l = []
        for item in range(len(obj)):
            l.append(obj.pop())
        return l

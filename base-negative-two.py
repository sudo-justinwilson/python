##This was a coding challenge I was asked to perform during an online technical interview..
##Unfortunately, I ran out of time before I got a chance to submit the solution, but I put it here for future reference...
##
##Challenge:
##Write a function that accepts an array (A) as an argument. A (the array) consists 1s and 0s. 
##It is like binary, 
##
##Binary (base 2) consists of ones and zeros, with the least signigicant numbers starting from the right most column. For each column that we move left, the value of units increase exponentially by 2:
##
##EG:
##    32  16  8   4   2   1
##
##The challenge is to write a function that accepts an array (A) as an argument, and consists of 1s and 0s (eg: [1,0,0,1,1], that is Base -2, and also with the LEAST signigicant numbers starting from the RIGHT most column (as opposed to binary, where the least significant number is in the leftmost column).
##The function should return an array that has the same format as the input, but returns the negative equivalent..
##
##INPUT:
##    An array consisting of binary integers (1s and 0s) representing a BASE -2 number, where the most significant numbers are in the right-most column.
##
##OUTPUT:
##    An array with the same form as the input, but representing the negative equivalent of the input value.
##
##EXAMPLE:
##    A = [1, 0, 0, 1, 1]
##    which is equal to decimal 9
##
##    X = solution(A)
##    # from memory the output should be [1,0,0,1,1,1] which should be equal to decimal -9 (base -2)??
##    X
##    [1,1,0,0,1,1]
##
###Here's what I have so far:
# To convert an array representing a base -2 sequence:
sum([A[i] * ((-2) ** i) for i in range(len(A))])

#To convert array A to it's decimal  negative equivalent:
sum([(j - j*2) for j in [A[i] * ((-2) ** i) for i in range(len(A))]])


 # TODO: I have to work out a way to convert the negative value into base -2??   
    To build up a base -2 table:
        [1*((-2)**i) for i in range(1,17)]

# from wikipedia:
def negaternary(i):
    digits = []
    if not i:
        digits = ['0']
    else:
        while i != 0:
            i, remainder = divmod(i, -2)
            if remainder < 0:
                i, remainder = i + 1, remainder + 2
            digits.append(str(remainder))
    return ''.join(digits[::-1])

if __name__ == '__main__':
    x = 9
    xx = negaternary(x)
    print('here is the result:\t', xx)


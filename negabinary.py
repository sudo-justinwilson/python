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

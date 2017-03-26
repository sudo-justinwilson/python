def to_negative_base(i, b):
    """
    This  function will convert an base 10 integer (signined & unsigned), to any base (negative or positive).
    ARGS:
        i = base 10 integer
        b = base of new number
    The result is returned as an array (list).

    """
    if not i:
        return [0]
    else:
        l = []
        while i != 0:
            i,r = divmod(i,b)
            if r < 0:
                i += 1
                r += abs(b)
            l.append(r)
        return l

if __name__ == '__main__':
    d = 9
    base = -2
    print(to_negative_base(d, base))
    

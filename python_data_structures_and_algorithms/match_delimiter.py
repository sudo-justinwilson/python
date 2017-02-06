from arraystacks import ArrayStack

"""
This is a program that ensures that delimiters such as "",[],(),{} are paired.
"""

def is_matched(expr):
    """
    Returns True if delimiters are properly paired.
    """
    lefty = '({['
    righty = ')}]'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()

if __name__ == '__main__':
    matched = 'for i in range(len(object)):print(i)'
    unmatched = 'for i in range(((len(object):print(i)'
    print('test function on a matched string: ')
    print(matched)
    print('Are the delimiters paired?')
    print(is_matched(matched))
    print('Now test the function on an unmatched delimiter: ')
    print(unmatched)
    print('Are the delimiters paired?')
    print(is_matched(unmatched))

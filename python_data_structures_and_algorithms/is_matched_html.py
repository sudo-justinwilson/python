from arraystacks import ArrayStack

def is_matched_html(raw):
    """
    Return True if all HTML tags match.

    raw is the raw HTML string.
    """
    S = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j + 1)
        if k == -1:
            return False
        tag = raw[j+1:k]    # this slice is the actual HTML tag
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k+1)
    return S.is_empty()

if __name__ == '__main__':

    s = """<body>
    <center>
    <h1> the Little Boat </h1>
    </center>
    </body>"""
    print("on a correct html string: ")
    print(s)
    print("is matched? ", is_matched_html(s))
    print("Now we will try with this html string: ")
    ss = """<body>
    <center>
    <h1> the Little Boat </h1>
    <center>
    </body>"""
    print(ss)
    print("is matched? ", is_matched_html(ss))


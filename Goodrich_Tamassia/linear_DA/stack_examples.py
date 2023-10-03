from Stack import ArrayStack


def reverse_file(filename):
    """Overwrite given file with its contents line-by-line reversed."""
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))  # we will re-insert newlines when writing
    original.close()

    # now we overwrite with contents in LIFO order
    output = open(filename, 'w')  # reopening file overwrites original
    while not S.is_empty():
        output.write(S.pop() + '\n')  # re-insert newline characters
    output.close()


# One technical detail worth noting is that we intentionally strip trailing newlines
# from lines as they are read, and then re-insert newlines after each line when writing
# the resulting file. Our reason for doing this is to handle a special case in which the
# original file does not have a trailing newline for the final line.
# In our implementation, we ensure that there will be a separating newline in the result.


# An Algorithm for Matching Delimiters

def is_matched(expr):
    """Return True if all delimiters are properly match; False otherwise."""
    lefty = '({['  # opening delimiters
    righty = ')}]'  # respective closing delims
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)  # push left delimiter on stack
        elif c in righty:
            if S.is_empty():
                return False  # nothing to match with
            if righty.index(c) != lefty.index(S.pop()):
                return False  # mismatched
    return S.is_empty()  # were all symbols matched?


def is_matched_html(raw: str):
    """Return True if all HTML tags are properly match; False otherwise."""
    S = ArrayStack()
    j = raw.find('<')  # find first ’<’ character (if any)
    while j != -1:
        k = raw.find('>', j + 1)  # find next ’>’ character
        if k == -1:
            return False  # invalid tag
        tag = raw[j + 1:k]  # strip away < >
        tag_name = tag.split(' ')[0]  # take only the name of the tag
        if not tag_name.startswith('/'):  # this is opening tag
            S.push(tag_name)
        else:  # this is closing tag
            if S.is_empty():
                return False  # nothing to match with
            if tag_name[1:] != S.pop():
                return False  # mismatched delimiter
        j = raw.find('<', k + 1)  # find next ’<’ character (if any)

    return S.is_empty()  # were all opening tags matched?

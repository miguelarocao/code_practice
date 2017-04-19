# Interview Cake: Bracket Validator
# https://www.interviewcake.com/question/python/bracket-validator
# Miguel Aroca-Ouellette
# 28/11/2016

def bracket_validator(string):
    pairs = { '(' :')', '{': '}', '[': ']'}
    openers = set(pairs.iterkeys())
    closers = set(pairs.itervalues())

    stack = []

    for c in string:
        if c in openers:
            stack.append(c)
        elif c in closers:
            if stack == [] or pairs[stack.pop()] != c:
                # does not match
                return False

    if stack != []:
        return False

    return True

# Test
print bracket_validator('{ [ ] ( ) }') == True
print bracket_validator('{ [ ( ] ) }') == False
print bracket_validator('{[}') == False
print bracket_validator(']') == False
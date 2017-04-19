# Interview Cake: Matching Parentheses
# https://www.interviewcake.com/question/python/matching-parens
# Miguel Aroca-Ouellette
# 02/03/2017

def match_parens(str, start):
    # Finds matching parentheses for the opening parenthesis specified by start

    if str[start] != '(':
        raise ValueError("Input must be starting parentheses.")

    count = 0
    for i, c in enumerate(str[start:]):
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
            if count < 0:
                raise RuntimeError("Unbalanced Parentheses")
            if count == 0:
                return i + start

    raise RuntimeWarning("No matching parentheses.")

str = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
print match_parens(str, 10)
# Interview Cake: Permutation Palindrome
# https://www.interviewcake.com/question/python/permutation-palindrome
# Miguel Aroca-Ouellette
# 28/11/2016


def perm_palindrome(str):
    """
    Returns True if any permutation of the input string is a palindrome.
    """

    unpaired = set()

    for c in str:
        if c in unpaired:
            unpaired.remove(c)
        else:
            unpaired.add(c)

    return len(unpaired) <= 1

# Test
print perm_palindrome('civic') == True
print perm_palindrome('ivicc') == True
print perm_palindrome('civil') == False
print perm_palindrome('livci') == False
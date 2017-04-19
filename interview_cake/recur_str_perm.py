# Interview Cake: Recursive String Permutations
# https://www.interviewcake.com/question/python/recursive-string-permutations
# Miguel Aroca-Ouellette
# 09/03/2017

def recur_str_perm(str, cache = None):
    # Finds all permutations of the input string
    # Base case
    if len(str) == 1:
        return {str[0]}

    if cache is None:
        cache = {}

    output = set() # Set of permutations
    for i, c in enumerate(str):
        key = str[:i] + str[i + 1:]
        if key not in cache:
            cache[key] = recur_str_perm(key, cache=cache)

        for p in cache[key]:
            output.add(c + p)

    return output

def recur_str_perm_better(str):
    # Finds all permutations of the input string
    # Same time complexity as above, but less memory & fewer function calls
    if len(str) == 1:
        return {str}

    perms = recur_str_perm(str[1:])

    output = set()
    for p in perms:
        for i in range(len(p) + 1):
            output.add(p[:i] + str[0] + p[i:])

    return output

print recur_str_perm('cat')
print recur_str_perm_better('cat')
# Interview Cake: Word Cloud
# https://www.interviewcake.com/question/python/word-cloud
# Miguel Aroca-Ouellette
# 14/09/2016

def word_counter(strings):
    """
    Counts the number of times each word appears in the input strings.
    :param strings: List of strings to parse.
    :return: Dictionary where keys are words and values are the number of occurences in the input.
    """
    # Note: Only iterates through the string once.

    output = {}
    for string in strings:
        new_word =""
        i = 0
        while i < len(string):
            c = string[i]
            print c
            if c.isalpha() or c == '-':
                new_word += c.lower()
            # else c is not alpha numeric
            else:
                if c == "'":
                    # Check for possessive modifier
                    if ((not string[i + 2].isalpha()) and string[i + 1] == 's') or \
                            ((not string[i + 1].isalpha()) and string[i - 1] == 's'):
                        i += 1 # Skip next letter
                    else:
                        # Contraction
                        new_word += c
                else:
                    # Add to dictionary if not empty
                    if new_word:
                        try:
                            output[new_word] += 1
                        except KeyError:
                            output[new_word] = 1

                        new_word = ""
            i += 1

    return output

test_strings = ['After beating the eggs, Dana read the next step:',
                'Add milk and eggs, then add flour and sugar.',
                "We came, we saw, we conquered ... then we ate Bill's (Mille-Feuille) cake."
                ]

print word_counter(test_strings)

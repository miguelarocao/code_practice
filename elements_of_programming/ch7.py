# Chapter 7 Problems

# Problem 7.2
def base_conversion(string, b1, b2):
    # Step 1: convert to base 10 (integer)
    exp = num = 0
    neg = False
    for i in range(len(string)):
        c = string[-(i + 1)]
        if (i == len(string) - 1) and c == '-':
            neg = True
            break
        num += to_int(c) * (b1 ** exp)
        exp += 1

    output = ''  # builds output backwards
    while num > 0:
        output += to_chr(num % b2)
        num /= b2

    if neg:
        output += '-'

    return output[::-1]


def to_int(c):
    # Returns an integer from a string number
    try:
        return int(c)
    except ValueError:
        return 10 + ord(c) - ord('A')


def to_chr(x):
    # Returns a char from a string
    return str(x) if x < 10 else chr(x - 10 + ord('A'))


# Problem 7.6
def reverse_words(string):
    # Step 1: Reverse Whole String
    for i in range(len(string) / 2):
        string[i], string[-(i + 1)] = string[-(i + 1)], string[i]

    # Step 2: Reverse Words
    word_start = 0
    word_end = 0
    while word_start < len(string):
        while word_end < (len(string)) and string[word_end] != ' ':
            word_end += 1

        for i in range((word_end - word_start) / 2):
            string[word_start + i], string[word_end - i - 1] = string[word_end - i - 1], string[word_start + i]

        # Handle multiple white space
        while word_end < (len(string)) and string[word_end] == ' ':
            word_end += 1

        word_start = word_end

    return string


# Problem 7.6 (Takes into account fact that strings are immutable in Python)
def reverse_words_immutable(string):
    # Step 1: Reverse Whole String
    reversed = string[::-1]
    output = ''

    # Step 2: Reverse Words
    word_start = 0
    word_end = 0
    while word_start < len(string):
        while word_end < (len(string)) and string[word_end] != ' ':
            word_end += 1

        output += reversed[word_end - 1:word_start - 1:-1]

        # Handle multiple white space
        while word_end < (len(string)) and string[word_end] == ' ':
            word_end += 1

        word_start = word_end

    return string


print base_conversion("-615", 7, 13)
print reverse_words(list("Alice likes Bob"))  # Pretend strings are mutable
print reverse_words_immutable("Alice likes Bob")

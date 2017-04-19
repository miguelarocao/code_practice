# Chapter 5 Problems

# Problem 5.8
def reverse_digits(x):
    neg = x < 0
    output = 0
    if neg:
        x *= -1

    while x:
        output *= 10
        output += x%10
        x /= 10

    return -output if neg else output

def test_15_8():
    print reverse_digits(43)
    print reverse_digits(-123)

def main():
    test_15_8()

if __name__ == '__main__':
    main()
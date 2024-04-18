# https://www.codechef.com/problems/FIBXOR01/
"""
Notes:
    TRICKY!!
"""


def custom_fib(n, a, b):
    if n == 0:
        return a
    elif n == 1:
        return b
    elif n == 2:
        return a ^ b

    return custom_fib(n % 3, a, b)


if __name__ == "__main__":
    print(custom_fib(15, 86, 77))  # o/p should be: 86
    print(custom_fib(86, 93, 35))  # o/p should be: 126
    print(custom_fib(21, 92, 49))  # o/p should be: 92
    print(custom_fib(90, 62, 27))  # o/p should be: 62

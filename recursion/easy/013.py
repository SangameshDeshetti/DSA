# https://www.geeksforgeeks.org/sum-digit-number-using-recursion/
def sum_digits_rec(number):
    if number == 0:
        return 0
    return number % 10 + sum_digits_rec(number // 10)


if __name__ == '__main__':
    num = 12345
    print(sum_digits_rec(num))

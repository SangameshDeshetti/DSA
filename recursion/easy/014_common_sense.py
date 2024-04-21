# https://www.geeksforgeeks.org/product-2-numbers-using-recursion/

def mul_2_nums_rec(num1, num2):
    if num2 == 0:
        return 0
    return num1 + mul_2_nums_rec(num1, num2 - 1)


if __name__ == '__main__':
    print(mul_2_nums_rec(124, 23))  # Assumption: num1 > num2

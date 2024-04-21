# https://www.geeksforgeeks.org/sum-of-natural-numbers-using-recursion/

def sum_n_numbers(num):
    if num == 0:
        return 0
    return num + sum_n_numbers(num - 1)


if __name__ == '__main__':
    print(sum_n_numbers(10))

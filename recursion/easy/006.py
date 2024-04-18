def print1_n(n):
    if n <= 0:
        return
    print1_n(n - 1)
    print(n, end=" ")


if __name__ == '__main__':
    print1_n(12)

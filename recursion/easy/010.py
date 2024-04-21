# https://www.geeksforgeeks.org/problems/geek-onacci-number/0

def geekonacci_num(a, b, c, n):
    if n == 1:
        return a
    if n == 2:
        return b
    if n == 3:
        return c
    return geekonacci_num(a, b, c, n - 1) + geekonacci_num(a, b, c, n - 2) + geekonacci_num(a, b, c, n - 3)


if __name__ == '__main__':
    print(geekonacci_num(1, 3, 2, 4))
    print(geekonacci_num(1, 3, 2, 5))
    print(geekonacci_num(1, 3, 2, 6))

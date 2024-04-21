# https://leetcode.com/problems/power-of-two/

def pow_2(num, arr=None):
    if arr is None:
        arr = []
    if num < 1:
        return False
    if num == 1:
        return True
    return num % 2 == 0 and pow_2(num // 2)


if __name__ == '__main__':
    print(pow_2(1024))

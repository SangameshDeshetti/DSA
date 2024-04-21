# https://leetcode.com/problems/power-of-four/

def pow_4(num):
    if num <= 0:
        return False
    if num == 1:
        return True
    elif num in [2, 3]:
        return False
    return num % 4 == 0 and pow_4(num // 4)


if __name__ == '__main__':
    print(pow_4(0))
    print(pow_4(1))
    print(pow_4(2))
    print(pow_4(3))
    print(pow_4(4))
    print(pow_4(-1))
    print(pow_4(16))
    print(pow_4(256))
    print(pow_4(512))
    print(pow_4(43))

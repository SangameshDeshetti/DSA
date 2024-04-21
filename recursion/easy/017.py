# https://leetcode.com/problems/power-of-two/

def pow_2(num):
    if num <= 0:
        return False
    if num == 1:
        return True
    return num % 2 == 0 and pow_2(num // 2)


if __name__ == '__main__':
    print(pow_2(0))
    print(pow_2(1))
    print(pow_2(2))
    print(pow_2(3))
    print(pow_2(42))
    print(pow_2(53))
    print(pow_2(128))
    print(pow_2(256))
    print(pow_2(-1))

# https://leetcode.com/problems/power-of-three/

def pow_3(num):
    if num <= 0:
        return False
    if num == 1:
        return True
    if num == 2:
        return False
    return num % 3 == 0 and pow_3(num // 3)


if __name__ == '__main__':
    print(pow_3(0))
    print(pow_3(1))
    print(pow_3(2))
    print(pow_3(3))
    print(pow_3(45))
    print(pow_3(81))
    print(pow_3(96))
    print(pow_3(27))
    print(pow_3(-1))

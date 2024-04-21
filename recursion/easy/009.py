# https://www.geeksforgeeks.org/program-for-length-of-a-string-using-recursion/

def string_length(string):
    if not string:
        return 0
    return 1 + string_length(string[1:])


if __name__ == '__main__':
    print(string_length("hello world"))

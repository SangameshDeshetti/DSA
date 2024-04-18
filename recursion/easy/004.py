# https://www.geeksforgeeks.org/first-uppercase-letter-in-a-string-iterative-and-recursive/

def first_upper_case(string: str, idx: int = None):
    if not string:
        return ""

    if idx is None:
        idx = 0

    if string[idx].isupper():
        return string[idx]
    else:
        return first_upper_case(string[1:])


if __name__ == '__main__':
    print(first_upper_case("hElloWorld"))

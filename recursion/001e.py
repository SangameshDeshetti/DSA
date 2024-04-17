"""
https://www.geeksforgeeks.org/sum-triangle-from-array/
"""


def sum_tri_from_list(lst):
    if not lst:
        return
    new_lst = [lst[i] + lst[i + 1] for i in range(len(lst) - 1)]
    sum_tri_from_list(new_lst)
    print(lst)


if __name__ == '__main__':
    sum_tri_from_list([1, 2, 3, 4, 5])

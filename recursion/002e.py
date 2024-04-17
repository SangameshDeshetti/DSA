# https://www.geeksforgeeks.org/recursive-programs-to-find-minimum-and-maximum-elements-of-array/


def min_max_in_list(lst, idx=0, minimum=None, maximum=None):
    if idx == len(lst):
        return [minimum, maximum]

    if not minimum and not maximum:
        minimum = maximum = lst[0]

    if lst[idx] > maximum:
        maximum = lst[idx]

    if lst[idx] < minimum:
        minimum = lst[idx]

    return min_max_in_list(lst, idx + 1, minimum, maximum)


def find_min(lst):
    if len(lst) == 1:
        return lst[0]
    return min(lst[0], find_min(lst[1:]))


if __name__ == '__main__':
    arr = [2, 5, 6, -1, -8, 0, 4, 12, -16]
    print(min_max_in_list(arr))
    print(find_min(arr))

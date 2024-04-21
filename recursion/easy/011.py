# https://www.geeksforgeeks.org/recursive-bubble-sort/

def bubble_sort_iterative(array):
    n = len(array) - 1
    for i in range(n):
        for j in range(i + 1, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]


def bubble_sort_rec(array, idx=0):
    n = len(array) - 1
    if idx == n - 1:
        return
    for j in range(idx + 1, n):
        if array[idx] > array[j]:
            array[idx], array[j] = array[j], array[idx]
    return bubble_sort_rec(array, idx + 1)


if __name__ == '__main__':
    arr = [0, 55, -3, 1, -1, 16, 89, 34, -43, 0, 9]
    print(arr)
    # bubble_sort_iterative(arr)
    bubble_sort_rec(arr)
    print(arr)

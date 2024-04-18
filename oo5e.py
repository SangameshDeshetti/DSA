# https://leetcode.com/problems/reverse-string/

def string_rev(array, idx=0):
    if not array:
        return
    end = len(array) - 1
    if idx <= end // 2:
        array[idx], array[end - idx] = array[end - idx], array[idx]
        string_rev(array, idx + 1)


if __name__ == '__main__':
    arr = ["h", "e", "l", "l"]
    print(arr)
    string_rev(arr)
    print(arr)

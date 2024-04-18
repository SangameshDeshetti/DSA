from typing import List


# https://leetcode.com/problems/binary-search/submissions/

def binary_search_rec(nums: List[int], target: int, start=None, end=None) -> int:
    if not nums:
        return -1

    if start is None and end is None:
        # The condition "if not start and not end:" is WRONG
        # Reason: if start or end is the index 0, then also it'll be True
        start, end = 0, len(nums) - 1

    if start > end:
        return -1

    mid = start + (end - start) // 2

    if target == nums[mid]:
        return mid
    elif target > nums[mid]:
        start = mid + 1
        return binary_search_rec(nums, target, start, end)
    else:
        end = mid - 1
        return binary_search_rec(nums, target, start, end)


if __name__ == '__main__':
    arr = [-1, 0, 2]
    tgt = -1
    print(binary_search_rec(arr, tgt))

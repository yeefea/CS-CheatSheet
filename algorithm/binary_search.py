"""
二分法
"""


def binary_search(n, nums: list):
    imin, imax = 0, len(nums) - 1
    while imin < imax:
        i = (imin + imax) // 2
        mid = nums[i]
        if mid > n:
            # i too large
            imax = i - 1
        elif mid < n:
            # i too small
            imin = i + 1
        else:
            return True

    return False


print(binary_search(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(binary_search(5, [1, 2, 3, 4, 6, 7, 8, 9, 10]))

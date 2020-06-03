"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

解题思路：哈希表
"""


def two_sum(nums: list, target: int) -> list:
    tmp_dict = {}  # value -> index
    for i, n in enumerate(nums):  # index, value
        if target - n in tmp_dict:
            return [tmp_dict[target - n], i]  # return [index0, index1]
        else:
            tmp_dict[n] = i  # store value -> index
    return []


print(two_sum([1, 3, 7, 4], 5))
print(two_sum([1, 3, 7, 4], 7))
print(two_sum([1, 3, 7, 4], 8))
print(two_sum([1, 3, 7, 4], 9))

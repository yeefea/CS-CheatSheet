"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
解题思路：
"""
class Solution:
    def threeSumClosest(self, num: List[int], target: int) -> int:
        min_distance = 1<<32
        num.sort()
        min_summation = 0

        for i, val in enumerate(num):
            j = i+1
            k = len(num)-1
            while j<k:
                lst = [val, num[j], num[k]]
                if min_distance>abs(target-sum(lst)):
                    min_summation = sum(lst)
                    if sum(lst)==target:
                        return min_summation
                    min_distance = abs(target-min_summation)
                elif sum(lst)>target:
                    k -= 1
                else:
                    j += 1
        return min_summation
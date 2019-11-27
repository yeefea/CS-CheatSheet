"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

解题思路：和15题类似，先排序，后两端向中间遍历
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = None
        residual = float('inf')
        nums.sort()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                tmp = [nums[i], nums[l], nums[r]]
                _sum = sum(tmp)
                if _sum == target:
                    return _sum
                tmp_residual = abs(_sum - target)
                if tmp_residual < residual:
                    residual = tmp_residual
                    res = _sum
                elif _sum > target:
                    r -= 1
                else:
                    l += 1
        return res

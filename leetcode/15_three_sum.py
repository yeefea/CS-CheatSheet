"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

解题思路：先排序O(NlogN)，后两端遍历O(N^2)
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            if nums[i] > 0:
                break
            left = i + 1  # 左指针
            right = len(nums) - 1  # 右指针
            while left < right:
                tmp = [nums[i], nums[left], nums[right]]
                _sum = sum(tmp)
                if _sum == 0:
                    result.append(tmp)
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:  # 跳过重复元素
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:  # 跳过重复元素
                        right -= 1
                elif _sum > 0:
                    right -= 1
                else:
                    left += 1

            i += 1
            while i < len(nums) - 2 and nums[i - 1] == nums[i]:  # 跳过重复元素
                i += 1
        return result

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

解题思路：先排序O(NlogN)，后两端遍历
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            l = i + 1
            r = len(nums) - 1
            while l < r:
                tmp = [nums[i], nums[l], nums[r]]
                _sum = sum(tmp)
                if _sum == 0:
                    result.append(tmp)
                    r -= 1
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:  # 跳过重复元素
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:  # 跳过重复元素
                        r -= 1
                elif _sum > 0:
                    r -= 1
                else:
                    l += 1

            i += 1
            while i < len(nums) - 2 and nums[i - 1] == nums[i]:  # 跳过重复元素
                i += 1
        return result

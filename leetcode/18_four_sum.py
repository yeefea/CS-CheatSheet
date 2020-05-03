"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

解题思路：先排序O(NlogN)，后分解为three sum问题
由此题可知：M-sum问题的通用解法复杂度为O(N**(M-1))
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4:
            return []
        result = []
        nums.sort()
        cur = 0
        while cur < len(nums) - 3:
            n = nums[cur]
            for x in self._three_sum(nums[cur + 1:], target - n):
                result.append([n] + x)
            cur += 1
            while cur < len(nums) - 3 and nums[cur - 1] == nums[cur]:  # 跳过重复元素
                cur += 1
        return result

    @classmethod
    def _three_sum(cls, nums: List[int], target: int):
        """
        类似于15题的逻辑
        :param nums: sorted list
        :param target:
        :return:
        """
        i = 0
        while i < len(nums) - 2:
            left = i + 1  # 左指针
            right = len(nums) - 1  # 右指针
            while left < right:
                tmp = [nums[i], nums[left], nums[right]]
                _sum = sum(tmp)
                if _sum == target:
                    yield tmp
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:  # 跳过重复元素
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:  # 跳过重复元素
                        right -= 1
                elif _sum > target:
                    right -= 1
                else:
                    left += 1
            i += 1
            while i < len(nums) - 2 and nums[i - 1] == nums[i]:  # 跳过重复元素
                i += 1

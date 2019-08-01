"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
解题思路：三指针
"""
from typing import List


class Solution:
    def threeSum(self, num: List[int]) -> List[List[int]]:
        result = []
        num.sort()  # sorting first, avoid duplicate,
        i = 0
        while i < len(num) - 2:
            j = i + 1
            k = len(num) - 1
            while j < k:
                lst = [num[i], num[j], num[k]]
                if sum(lst) == 0:
                    result.append(lst)
                    k -= 1
                    j += 1
                    # JUMP remove duplicate
                    while j < k and num[j] == num[j - 1]:
                        j += 1
                    while j < k and num[k] == num[k + 1]:
                        k -= 1
                elif sum(lst) > 0:
                    k -= 1
                else:
                    j += 1

            i += 1
            # remove duplicate
            while i < len(num) - 2 and num[i] == num[i - 1]:
                i += 1

        return result

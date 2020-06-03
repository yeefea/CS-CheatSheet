"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

    所有数字（包括目标数）都是正整数。
    解集不能包含重复的组合。

示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

解题思路：

去重很重要，如何去掉一个数组中重复的元素
除了使用哈希表以外，我们还可以先对数组升序排序，重复的元素一定不是排好序以后的第 1 个元素和相同元素的第 1 个元素。
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []
        # 排序
        candidates.sort()
        return self._combination(0, candidates, target)

    def _combination(self, start, candidates, target):
        res = []

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            n = candidates[i]
            new_target = target - n
            if new_target < 0:
                break
            if new_target == 0:
                res.append([n])
                continue
            tmp = self._combination(i + 1, candidates, new_target)
            for x in tmp:
                res.append([n] + x)
        return res


if __name__ == '__main__':
    sol = Solution()
    ans = sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    print(ans)

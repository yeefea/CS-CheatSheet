"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

解题思路：
二分查找法
分割后一部分是有序的，另一部分可能不是有序的
有序的部分可以根据两个端点判断数字是否在范围内，不在范围内则返回-1
在范围内，或者不是有序的，则继续分割
直到只有1个元素，停止分割，此时可以直接判断数组是否包含target数字
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        if l == 0:
            return -1
        return self._search(nums, 0, l - 1, target)

    def _search(self, nums, left, right, target):
        lv = nums[left]
        if left == right:
            if lv == target:
                return left
            else:
                return -1
        if left < right:
            rv = nums[right]
            if lv < rv:
                # 升序排列
                if lv > target or rv < target:
                    return -1
                if lv == target:
                    return left
                if rv == target:
                    return right
            # 继续分割
            mid = (left + right) >> 1
            return max(self._search(nums, left, mid, target), self._search(nums, mid + 1, right, target))
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.search([1, 2, 3, 4], 4))
    print(sol.search([0], 1))

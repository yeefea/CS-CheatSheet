"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

解题思路：

一开始沒理解题目的意思，是看了解答之后才理解的。字典序中下一个更大的序列就是可以排列出的下一个更大的数字。
比如1 2 3 4下一个是1 2 4 3，下一个是1 3 2 4，下一个是1 3 4 2
举例：
1 3 4 2 -> 1 4 2 3
首先从后往前找升序对(i,j)，找到(3,4)，可以得知j(包含)之后的数字都是降序的
然后从后往前找比3大的最小的数字，找到4，交换3和4
最后将j到末尾的数字升序排列，两两首尾交换即可
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) < 2:
            return
        i = len(nums) - 2
        j = i + 1
        k = j
        while i > -1:
            if nums[i] < nums[j]:
                break
            i -= 1
            j -= 1
        if i > -1:
            while nums[i] >= nums[k]:
                k -= 1
            nums[i], nums[k] = nums[k], nums[i]
        # 当i=-1时说明整个列表是降序排列的，是最后一个排列，此时j=0只需要将列表从0到末尾倒序即可
        k = len(nums) - 1
        while j < k:
            nums[j], nums[k] = nums[k], nums[j]
            j += 1
            k -= 1


if __name__ == '__main__':
    sol = Solution()
    lst = [1, 2, 4, 3]
    sol.nextPermutation(lst)
    print(lst)

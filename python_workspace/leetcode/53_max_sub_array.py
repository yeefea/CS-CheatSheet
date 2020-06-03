"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


def max_sub_array(nums: List[int]) -> int:
    """
    分治法，O(NlogN)时间复杂度，非最优
    :param nums:
    :return:
    """
    len_arr = len(nums)
    if len_arr == 1:  # 递归终止条件
        return nums[0]
    mid = len_arr // 2  # 从i处分割数组，分成左右两部分[-2,1,-3,4] [-1,2,1,-5,4]
    max_l = nums[mid - 1]  # 记录左边数组的最大值
    tmp = 0  # 记录临时最大值
    for i in range(mid - 1, -1, -1):
        tmp += nums[i]
        max_l = max(max_l, tmp)
    max_r = nums[mid]
    tmp = 0
    for i in range(mid, len_arr):
        tmp += nums[i]
        max_r = max(max_r, tmp)
    return max(max_sub_array(nums[:mid]), max_sub_array(nums[mid:]), max_l + max_r)


def max_sub_array_dynamic_programming(nums):
    """
    从最简单的情况开始分析
    [-2] 只有一个元素，最大只能是-2
    [-2, 1] 最大和是 1 + 1之前的子序列的最大和， 或者是1本身，二者选较大值
    [-2, 1, -3] 最大和是 -3 + -3之前的子序列的最大和，或者是-3本身，二者选较大值
    动态规划
    :param nums:
    :return:
    """
    max_sum = nums[0]
    best_cache = [0] * len(nums)
    best_cache[0] = max_sum
    for i in range(1, len(nums)):
        tmp = max(best_cache[i - 1] + nums[i], nums[i])
        best_cache[i] = tmp
        if max_sum < tmp:
            max_sum = tmp
    return max_sum


def max_sub_array_kadane(nums):
    """
    Kadane算法
    也是动态规划思想
    :param nums:
    :return:
    """
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
    return max(nums)


print(max_sub_array_kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

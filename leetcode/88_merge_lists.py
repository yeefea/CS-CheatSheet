"""
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

    初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
    你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    ptr = m + n - 1
    m -= 1
    n -= 1
    while ptr > -1:
        if n < 0:
            break
        if m < 0:
            nums1[:ptr + 1] = nums2[:ptr + 1]
            break
        if nums1[m] > nums2[n]:
            nums1[ptr] = nums1[m]
            m -= 1
        else:
            nums1[ptr] = nums2[n]
            n -= 1
        ptr -= 1


if __name__ == '__main__':
    arr1 = [1, 2, 3, 0, 0, 0]
    n1 = 3
    arr2 = [2, 5, 6]
    n2 = 3
    merge(arr1, n1, arr2, n2)
    print(arr1)

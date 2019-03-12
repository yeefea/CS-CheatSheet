"""
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。

解题思路：偏序关系，排序
"""
class ComparableStr(str):

    def __lt__(self, other):  # Trick!
        return int(self + other) < int(other + self)


def largest_num(nums):
    if len(nums) < 1:
        return '0'
    nums = [ComparableStr(x) for x in nums]
    largest_num = ''.join(sorted(nums, reverse=True))
    return '0' if largest_num[0] == '0' else largest_num


if __name__ == '__main__':
    nums = []
    print(largest_num(nums))
    nums = [0, 0, 0]
    print(largest_num(nums))
    nums = [10, 2]
    print(largest_num(nums))
    nums = [3, 30, 34, 5, 9]
    print(largest_num(nums))

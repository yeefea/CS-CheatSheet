"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

解题思路：暴力解法，int转字符串后反转，判断是否和原来的数相等。
"""


def is_palindrome_str(x: int) -> bool:
    if x < 0:
        return False
    elif x != int(str(x)[::-1]):
        return False
    else:
        return True


def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    y = 0
    tmp = x
    while tmp != 0:
        remainder = tmp % 10
        y = y * 10 + remainder
        tmp = tmp // 10
    return round(y) == x


print(is_palindrome(-1))
print(is_palindrome(101))

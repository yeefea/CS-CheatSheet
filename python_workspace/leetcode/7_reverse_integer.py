"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

解题思路：暴力解法，把int转成字符串反转后再转回int
"""


def reverse(x: int):
    """
    x为32位整数，可以表示-2^31 ~ 2^31-1
    :param x:
    :return:
    """
    y, res = abs(x), 0
    of = (1 << 31) - 1 if x > 0 else 1 << 31
    while y != 0:
        res = res * 10 + y % 10
        if res > of:
            return 0
        y //= 10
    return res if x > 0 else -res


def reverse_use_string(x):
    """
    :type x: int
    :rtype: int
    """
    mark = 1 if x >= 0 else -1
    x_abs = abs(x)
    result = mark * int(str(x_abs)[::-1])
    return result if -((1 << 31) - 1) <= result <= (1 << 31) else 0


print(reverse(123))
print(reverse(-123))

print(reverse_use_string(123))
print(reverse_use_string(-123))

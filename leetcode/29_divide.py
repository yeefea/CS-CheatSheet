"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divide-two-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

解题思路：二分法
边界值处理，测试集和题目有点不同，溢出时要返回-2^31或2^31-1
"""
_MIN = -1 * (1 << 31)
_MAX = (1 << 31) - 1


def positive_divide(dividend, divisor):
    ll = 0
    rr = dividend
    while True:
        mid = (ll + rr) >> 1
        remain = dividend - mid * divisor
        if remain < 0:
            rr = mid
        elif remain < divisor:
            return mid
        else:
            ll = mid + 1


class Solution:

    def divide(self, dividend: int, divisor: int) -> int:
        """

        """
        if dividend == 0:
            return 0

        if divisor > 0:
            sign = 1
        else:
            sign = -1
            divisor = -divisor

        if dividend < 0:
            sign = -1 * sign
            dividend = -dividend

        res = positive_divide(dividend, divisor)
        res = sign * res
        if _MIN <= res <= _MAX:
            return res
        elif res < 0:
            return _MIN
        else:
            return _MAX

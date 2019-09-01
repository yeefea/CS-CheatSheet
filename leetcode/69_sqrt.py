"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2

示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def sqrt(x: int) -> int:
    """
    指数递增寻找上界
    二分法寻找精确值
    :param x:
    :return:
    """
    if x == 0:
        return 0
    r = 1
    while True:
        r <<= 1
        if r * r == x:
            return r
        if r * r > x:
            break
    l = r >> 1

    while l < r:
        mid = (l + r) // 2
        sq = mid * mid
        if sq == x:
            return mid
        if sq > x:
            if mid == r:  # converge
                return r - 1
            r = mid
        else:
            if mid == l:  # converge
                return l
            l = mid
    return l


def sqrt_newton_raphson(x: int) -> int:
    res = 1
    while True:
        tmp = res - (res * res - x) / (res * 2)
        if abs(res - tmp) < 1e-6:  # converge
            break
        res = tmp
    return int(res)

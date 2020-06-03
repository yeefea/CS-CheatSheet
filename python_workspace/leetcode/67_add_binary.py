"""
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"

示例 2:

输入: a = "1010", b = "1011"
输出: "10101"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-binary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def add_binary_trick(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]


def add_binary(a: str, b: str) -> str:
    if len(b) > len(a):
        a, b = b, a  # a always longer than b
    diff_len = len(a) - len(b)
    if diff_len:
        b = '0' * diff_len + b
    res = []
    add = 0
    for b1, b2 in zip(reversed(a), reversed(b)):
        add, tmp = divmod(int(b1) + int(b2) + add, 2)
        res.append(str(tmp))
    if add == 1:
        res.append('1')
    res.reverse()
    return ''.join(res)


print(add_binary('1', '11'))

"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int n_rows);
示例 1:

输入: s = "LEETCODEISHIRING", n_rows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", n_rows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G

解题思路：index, step两个变量
"""


def convert(s: str, n_rows: int) -> str:
    if n_rows == 1 or n_rows >= len(s):
        return s
    res = [''] * n_rows
    idx, step = 0, 1

    for x in s:
        res[idx] += x
        if idx == 0:
            step = 1
        elif idx == n_rows - 1:
            step = -1
        idx += step
    return ''.join(res)


print(convert('LEETCODEISHIRING', 3))
print(convert('LEETCODEISHIRING', 4))

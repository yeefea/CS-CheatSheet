"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
解题思路：动态规划
"""


def longest_palindrome_dynamic_programming(s: str) -> str:
    ans = ''
    max_len = 0
    n = len(s)
    """
    [n x n]状态矩阵
    表示[l,r]子串(从l到r,包括端点)是否为回文子串
    其实对角线以下的区域是没有用的
    """
    dp = [[0] * n for _ in range(n)]

    """
    长度为1必定是回文串
    [
        T F F F F
        F T F F F
        F F T F F
        F F F T F
        F F F F T
                    ]
    """
    for i in range(n):  # 初始值1
        dp[i][i] = True
        max_len = 1
        ans = s[i]

    # 长度为2的回文串
    for i in range(n - 1):  # 初始值2
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            ans = s[i:i + 2]
            max_len = 2

    for i in range(n - 2, -1, -1):
        for j in range(i + 2, n):
            """
            状态转移函数!
            必须两个端点值相同，并且内部的字串是回文串
            """
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                ll = j - i + 1
                if ll > max_len:
                    max_len = ll
                    ans = s[i:j + 1]

    return ans


print(longest_palindrome_dynamic_programming('babad'))
print(longest_palindrome_dynamic_programming('ccc'))
print(longest_palindrome_dynamic_programming('cbbd'))

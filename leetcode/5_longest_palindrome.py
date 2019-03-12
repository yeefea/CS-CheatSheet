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
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        max_len = 0
        n = len(s)
        DP = [[0] * n for _ in range(n)]
        for i in range(n):
            DP[i][i] = True
            max_len = 1
            ans = s[i]
        for i in range(n-1):
            if s[i] == s[i+1]:
                DP[i][i+1] = True
                ans = s[i:i+2]
                max_len = 2
        for j in range(n):
            for i in range(0, j-1):
                if s[i] == s[j] and DP[i+1][j-1]:
                    DP[i][j] = True
                    if max_len < j - i + 1:
                        ans = s[i:j+1]
                        max_len = j - i + 1
        return ans
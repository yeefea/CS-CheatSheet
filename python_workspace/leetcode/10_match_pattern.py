"""
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素

所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:

    s 可能为空，且只包含从 a-z 的小写字母。
    p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。

示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false

解题思路：
.匹配

*匹配

"""


class Solution:

    def isMatch(self, text: str, pattern: str) -> bool:
        if text:
            if not pattern:
                return False
        else:
            if pattern:
                return False
            else:
                return True

        p0 = pattern[0]
        match = True if p0 == '.' else (p0 == text[0])

        if len(pattern) > 1 and pattern[1] == '*':
            return (match and self.isMatch(text[1:], pattern)) or self.isMatch(text, pattern[2:])
        else:
            return match and self.isMatch(text[1:], pattern[1:])

    def is_match_naive(self, text: str, pattern: str) -> bool:
        """
        naive!
        :param text:
        :param pattern:
        :return:
        """
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

    def is_match_memo(self, text: str, pattern: str) -> bool:
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j + 1 < len(pattern) and pattern[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

    def is_match(self, text, pattern):
        pass


def is_match(text, pattern):
    if not pattern:
        return not text
    p0 = pattern[0]
    match = bool(text) and (True if p0 == '.' else (p0 == text[0]))
    if len(pattern) > 1 and pattern[1] == '*':
        return (match and is_match(text[1:], pattern)) or is_match(text, pattern[2:])
    else:
        return match and is_match(text[1:], pattern[1:])


print(is_match('aa', 'a*'))

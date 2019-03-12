"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

解题思路：双指针，滑动窗口
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        
        l, r = 0, 0
        res, lookup = 0, set()
        while l < len(s) and r < len(s):
            if s[r] not in lookup:
                lookup.add(s[r])
                res = max(res, r-l+1)
                r += 1
            else:
                lookup.discard(s[l])
                l += 1
        return res
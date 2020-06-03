class Solution:

    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        res = s.strip().rsplit(' ', 1)
        return len(res[0]) if len(res) == 1 else len(res[1])

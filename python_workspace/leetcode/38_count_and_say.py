from itertools import groupby


class Solution:
    def countAndSay(self, n: int) -> str:
        n_str = '1'
        for _ in range(n - 1):
            n_str = ''.join('{}{}'.format(len(list(g)), x) for x, g in groupby(n_str))
        return n_str

's '.strip(' ')
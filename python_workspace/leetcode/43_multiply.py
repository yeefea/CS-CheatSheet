class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        if len(num2) > len(num1):
            num1, num2 = num2, num1
        res = 0
        multiplier = 1
        for x in reversed(num2):
            tmp = self._mul(num1, x)
            res += tmp * multiplier
            multiplier *= 10
        return str(res)

    def _mul(self, x, i):
        i = int(i)
        res = 0
        c = 0  # 进位
        multiplier = 1
        for a in reversed(x):
            a = int(a)
            c, r = divmod(a * i + c, 10)
            res += r * multiplier
            multiplier *= 10
        if c != 0:
            res += c * multiplier
        return res


if __name__ == '__main__':
    sol = Solution()
    ans = sol.multiply('123', '456')
    print(ans)

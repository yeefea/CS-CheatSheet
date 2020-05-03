from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0 or len(nums) == 1:
            return [nums[:]]
        res = []
        for i in range(len(nums)):
            n = nums[i]
            tmp = self.permute(nums[:i] + nums[i + 1:])
            for x in tmp:
                res.append([n] + x)
        return res


if __name__ == '__main__':
    sol = Solution()
    ans = sol.permute([1, 2, 3])
    print(ans)

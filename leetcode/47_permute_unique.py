from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """

        :param nums:
        :return:
        """
        # 去重首先想到要排序
        nums.sort()
        self.res = []
        self.recur(nums, [])
        return self.res

    def recur(self, nums, temp):
        if nums == []:
            self.res.append(temp)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.recur(nums[:i] + nums[i + 1:], temp + [nums[i]])


if __name__ == '__main__':
    sol = Solution()
    ans = sol.permuteUnique([1, 1, 2])
    print(ans)

"""

backtrack
"""
class Solution:
    def subsets(self, nums):
        def backtrack(k, first, curr):
            """

            :param k: length of subset
            :param first: first index
            :param curr: current elements
            :return:
            """
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])  # copy
                # cut
                return
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(k, i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            # subset with length k
            backtrack(k, 0, [])
        return output


if __name__ == '__main__':
    sol = Solution()

    res = sol.subsets([1, 2, 3,4])
    print(res)

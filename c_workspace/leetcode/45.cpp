#include <vector>
#include <iostream>
using namespace std;


/*
官方答案是贪心算法
这里用了动态规划，因为有状态转移和重叠子问题

要跳到最后一格的步数最少，要找到之前某个格子可以跳到最后一格，并且步数最少，依次递归。

可以用动态规划表dp，dp[i]存的是跳到每一格需要的最少步数。
*/

class Solution
{
public:

    int jump(vector<int> &nums)
    {
        if (nums.size() < 2)
        {
            return 0;
        }
        if (nums.size() == 2)
        {
            return 1;
        }

        vector<int> dp(nums.size(), 0);
        int max_idx = nums.size() - 1;
        // init jump
        for (int i = 1; i <= min(nums[0], max_idx); ++i)
        {
            dp[i] = 1;
        }
        for (int i = 1; i < nums.size() - 1; ++i)
        {
            if (dp[i] == 0)
            {
                // no jump
                continue;
            }
            int right = i + nums[i];
            if (max_idx < right)
            {
                right = max_idx;
            }
            for (int j = i + 1; j <= right; j++)
            {
                if (dp[j] == 0)
                {
                    dp[j] = dp[i] + 1;
                }
                else
                {
                    dp[j] = min(dp[i] + 1, dp[j]);
                }
            }
        }
        return dp[max_idx];
    }
};

int main(int argc, char const *argv[])
{
    Solution sol;

    vector<int> nums = {3, 2, 3, 1};
    auto res = sol.jump(nums);
    cout << "res = " << res << endl;
    return 0;
}

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution
{
public:
    bool isMatch(string s, string p)
    {
        int s_size = s.size(), p_size = p.size();
        if (s_size == 0 && p_size == 0)
        {
            return true;
        }
        if (s_size != 0 && p_size == 0)
        {
            return false;
        }

        vector<vector<int>> dp(s_size + 1, vector<int>(p_size + 1));
        dp[0][0] = true;
        // 最左边一列总是false

        for (int i = 0; i <= s_size; ++i)
        {
            for (int j = 1; j <= p_size; ++j)
            {
                if (p[j - 1] == '*')
                {
                    dp[i][j] |= dp[i][j - 2];
                    if (matches(s, p, dp, i, j - 1))
                    {
                        dp[i][j] |= dp[i - 1][j];
                    }
                }
                else
                {
                    if (matches(s, p, dp, i, j))
                    {
                        dp[i][j] |= dp[i - 1][j - 1];
                    }
                }
            }
        }

        return dp[s_size][p_size];
    }

    bool matches(string &s, string &p, vector<vector<int>> &dp, int i, int j)
    {
        // 关键函数
        if (i == 0)
        {
            return false;
        }
        if (p[j - 1] == '.')
        {
            return true;
        }
        return s[i - 1] == p[j - 1];
    }
};

int main(int argc, char const *argv[])
{

    return 0;
}

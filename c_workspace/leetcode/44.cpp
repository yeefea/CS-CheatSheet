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
        // "" and "" => true
        if (s_size == 0 && p_size == 0)
            return true;
        // "" and "***" => true, "" and "as****" => false
        if (s_size == 0 && p_size != 0)
        {
            for (auto &ch : p)
            {
                if (ch != '*')
                {
                    return false;
                }
            }
            return true;
        }
        // "aaaa" and "" => false
        if (s_size != 0 && p_size == 0)
            return false;

        vector<vector<int>> dp(s_size + 1, vector<int>(p_size + 1));
        dp[0][0] = true;
        for (int j = 1; j <= p_size; ++j)
        {
            if (p[j - 1] == '*')
            {
                dp[0][j] = true;
            }
            else
            {
                break;
            }
        }

        for (int i = 1; i <= s_size; ++i)
        {
            for (int j = 1; j <= p_size; ++j)
            {
                if (p[j - 1] == '*')
                {
                    dp[i][j] = dp[i][j - 1] | dp[i - 1][j];
                }
                else if (p[j - 1] == '?' || s[i - 1] == p[j - 1])
                {
                    dp[i][j] = dp[i - 1][j - 1];
                }
            }
        }

        return dp[s_size][p_size];
    }
};

int main(int argc, char const *argv[])
{
    Solution sol;
    auto res = sol.isMatch("ab", "***a?");
    cout << res << endl;
    return 0;
}

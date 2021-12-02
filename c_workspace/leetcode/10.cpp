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
        

        return dp[s_size][p_size];
    }
};

int main(int argc, char const *argv[])
{

    return 0;
}

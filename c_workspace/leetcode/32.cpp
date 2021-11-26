#include <algorithm>
#include <iostream>
#include <string>

using namespace std;
class Solution {
public:
    int longestValidParentheses(string s) {
        if (s.size() < 2) return 0;
        int dp[s.size()];
        dp[0] = 0;
        char ch;
        int ii;
        for (int i = 1; i < s.size(); ++i){
            ch = s[i];
            if (ch == '('){
                dp[i] = 0;
                continue;
            }
            if (s[i-1]== '('){
                ii = i - 2;
                dp[i] = ii < 0 ? 2 : dp[ii] + 2;
                continue;
            }

            ii = i - dp[i-1] - 1;
            if (ii < 0 || s[ii] == ')'){
                dp[i] = 0;
                continue;
            }
            dp[i] = dp[i-1] + 2;
            if (ii >0)
                dp[i] += dp[ii-1];
        }
        return *max_element(dp, dp+s.size());
    }
};

int main(int argc, char const *argv[])
{
    Solution sol;
    string s = ")((()))";
    auto res = sol.longestValidParentheses(s);
    cout << res << endl;
    return 0;
}

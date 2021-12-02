#include <vector>
#include <iostream>
#include <algorithm>
/*
 * 双指针思想
 * 累积最值 cumulative max,min
 */
using namespace std;

class Solution
{
public:
    int trap(vector<int> &height)
    {
        if (height.size() < 3)
        {
            return 0;
        }
        int max_idx = 0; // argmax
        int max = 0;
        for (int i = 0; i < height.size(); ++i)
        {
            if (height[i] > max)
            {
                max = height[i];
                max_idx = i;
            }
        }

        int volumn = 0, h;
        max = height[0];
        // left ->
        for (int i = 1; i <= max_idx; ++i)
        {
            h = height[i];
            if (h < max)
            {
                volumn += max - h;
            }
            else if (h > max)
            {
                max = h;
            }
        }
        // <- right
        max = height[height.size() - 1];
        for (int i = height.size() - 2; i > max_idx; --i)
        {
            h = height[i];
            if (h < max)
            {
                volumn += max - h;
            }
            else if (h > max)
            {
                max = h;
            }
        }
        return volumn;
    }
};

int main(int argc, char const *argv[])
{
    Solution sol;
    vector<int> vec = {4, 2, 0, 3, 2, 5};
    auto res = sol.trap(vec);

    cout << res << endl;
    return 0;
}

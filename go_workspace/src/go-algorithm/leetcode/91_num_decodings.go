// +build ignore

package main

import (
	"fmt"
	"strconv"
)

func main() {
	ss := []string{"0", "1", "2", "3", "01", "02", "10", "20", "30", "11", "12", "123"}
	for _, s := range ss {
		fmt.Println(numDecodings(s))
	}

}

/*
91. 解码方法
一条包含字母 A-Z 的消息通过以下方式进行了编码：
'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

思路: 动态规划,考虑0的多种情况
*/
func numDecodings(s string) int {
	if len(s) == 0 {
		return 0
	}
	if s[0] == '0' {
		return 0
	}
	dpN1, dpN2 := 1, 1 // dp[n-1], dp[n-2]

	if len(s) == 1 {
		return dpN2
	}
	for n := 1; n < len(s); n++ {
		var tmp int
		if s[n] == '0' {
			if s[n-1] == '1' || s[n-1] == '2' {
				// "...10" or "...20"
				tmp = dpN2
			} else {
				// "...00", "..30", "...40",...
				return 0
			}
		} else {
			i, _ := strconv.Atoi(s[n-1 : n+1])
			if i < 10 {
				tmp = dpN1
			} else if i < 27 {
				tmp = dpN1 + dpN2
			} else {
				tmp = dpN1
			}
		}
		dpN2 = dpN1
		dpN1 = tmp
	}
	return dpN1
}

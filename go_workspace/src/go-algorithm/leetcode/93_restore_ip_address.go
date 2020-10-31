// +build ignore

package main

import (
	"fmt"
	"strconv"
	"strings"
)

/*
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。



示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

思路: 回溯算法，递归，剪支

边界情况要想清楚，IP地址分为4段
最长3位数，最大255，遇到某位是0则该段只能是"0"，要跳过后续"01","011"之类的情况
*/

func restoreIpAddresses(s string) []string {
	res := make([]string, 0)
	backtrack(4, []string{}, s, &res)
	return res
}

func backtrack(nSplit int, prefix []string, remain string, res *[]string) {
	if nSplit == 0 {
		if remain == "" {
			*res = append(*res, strings.Join(prefix, "."))
		}
		return
	}
	for i := 0; i < 3 && i < len(remain); i++ {
		tmp, _ := strconv.Atoi(remain[:i+1])
		if tmp > 255 {
			break
		}
		prefix = append(prefix, remain[:i+1])
		// backtrack
		backtrack(nSplit-1, prefix, remain[i+1:], res)
		prefix = prefix[:len(prefix)-1]
		// 10.12.0.1
		// if 0 then break
		if tmp == 0 {
			break
		}
	}
}
func main() {
	res := restoreIpAddresses("25525511135")
	fmt.Println(res)
	res = restoreIpAddresses("010010")
	fmt.Println(res)
}

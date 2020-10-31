// +build ignore

package main

import "fmt"

/*
131. 分割回文串
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
解题思路:回溯法
*/
func main() {
	s := "aab"
	fmt.Println(partition(s))
}

func partition(s string) [][]string {
	// 最终结果列表
	res := make([][]string, 0)
	// 从0开始回溯
	backtrack(s, 0, []string{}, &res)
	// 返回最终结果列表
	return res
}

// backtrack 回溯
func backtrack(s string, start int, prefix []string, res *[][]string) {
	/*
		s 字符串
		start 开始坐标
		prefix 临时结果
		res 最终结果列表
	*/
	if start == len(s) {
		tmp := make([]string, len(prefix))
		// 复制数组
		copy(tmp, prefix)
		// 添加到最终结果列表
		*res = append(*res, tmp)
		return
	}
	for i := start; i < len(s); i++ {
		// start到i子串
		tmp := s[start : i+1]
		if !isPalindrome(tmp) {
			// 不是回文串则剪枝
			continue
		}
		// 添加回文串到临时结果集
		prefix = append(prefix, tmp)
		// 回溯
		backtrack(s, i+1, prefix, res)
		// 去掉刚添加的回文串
		prefix = prefix[:len(prefix)-1]
	}
}

func isPalindrome(s string) bool {
	// 首尾两个字符相比较
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		if s[i] != s[j] {
			// 如果有任何一位不相同,则不是回文串,立即返回false
			return false
		}
	}
	// 收尾字符都相同,是回文串
	return true
}

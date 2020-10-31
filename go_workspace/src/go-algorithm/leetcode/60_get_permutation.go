// +build ignore

package main

import (
	"fmt"
	"strconv"
	"strings"
)

/*
60. 第k个排列
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"

思路:回溯法,但是比较慢

todo 考虑更好的方法
*/
func getPermutation(n int, k int) string {
	pre := []int{}
	remain := make([]int, n)
	for i := 0; i < n; i++ {
		remain[i] = i + 1
	}
	kk := k
	res := backtrack(pre, remain, &kk)
	s := make([]string, len(res))
	for i := 0; i < len(res); i++ {
		s[i] = strconv.Itoa(res[i])
	}
	return strings.Join(s, "")
}

func backtrack(prefix []int, remain []int, k *int) []int {
	if len(remain) == 0 {
		*k--
		if *k == 0 {
			return prefix
		}
		return nil
	}
	for i := 0; i < len(remain); i++ {
		prefix = append(prefix, remain[i])
		res := backtrack(prefix, join(remain[:i], remain[i+1:]), k)
		if res != nil {
			return res
		}
		prefix = prefix[:len(prefix)-1]
	}
	return nil
}
func join(x, y []int) []int {
	res := make([]int, len(x)+len(y))
	i := 0
	for ; i < len(x); i++ {
		res[i] = x[i]
	}
	for j := 0; j < len(y); j++ {
		res[i] = y[j]
		i++
	}
	return res
}

func main() {
	fmt.Println(getPermutation(3, 3))
	fmt.Println(getPermutation(4, 9))
}

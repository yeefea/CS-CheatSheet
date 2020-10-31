// +build ignore

package main

import "fmt"

/*
120. 三角形最小路径和
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
例如，给定三角形：
[
[2],
[3,4],
[6,5,7],
[4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
说明：
如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分

思路:动态规划,如果原始三角形可以修改的话可以只使用O(1)额外空间
这里不修改原始三角形,用额外的O(n)空间
*/
func minimumTotal(triangle [][]int) int {
	if len(triangle) == 0 {
		return 0
	}
	if len(triangle) == 1 {
		return triangle[0][0]
	}
	dp := triangle[0]
	for i := 1; i < len(triangle); i++ {
		tmpDp := make([]int, i+1)
		tmpDp[0] = triangle[i][0] + dp[0]
		tmpDp[i] = triangle[i][i] + dp[i-1]
		for j := 1; j < i; j++ {
			tmpDp[j] = triangle[i][j] + getAdjcentMinValue(dp, i, j)
		}
		dp = tmpDp
	}
	return min(dp)
}

func min(nums []int) int {
	res := nums[0]
	for i := 1; i < len(nums); i++ {
		if nums[i] < res {
			res = nums[i]
		}
	}
	return res
}
func getAdjcentMinValue(dp []int, i, j int) int {
	if j == 0 {
		return dp[0]
	}
	if j == i {
		return dp[j-1]
	}
	if dp[j-1] < dp[j] {
		return dp[j-1]
	}
	return dp[j]
}

func main() {
	t := make([][]int, 4)
	t[0] = []int{2}
	t[1] = []int{3, 4}
	t[2] = []int{6, 5, 7}
	t[3] = []int{4, 1, 8, 3}
	res := minimumTotal(t)
	fmt.Println(res)
	fmt.Println(t[5:])
}

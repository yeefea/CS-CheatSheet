package main

import (
	"fmt"
	"go-algorithm/leetcode"
)

func main() {
	// res := leetcode.SimplifyPath("/home/")
	// fmt.Println(res)
	// res := leetcode.GroupAnagrams([]string{"abc", "cba", "bcd"})
	// fmt.Println(res)
	// s := make([]int, 0)
	// fmt.Println(s)
	// matrix := make([][]int, 3)
	// matrix[0] = []int{1, 2, 3, 4, 5}
	// matrix[1] = []int{6, 7, 8, 9, 10}
	// matrix[2] = []int{11, 12, 13, 14, 15}
	// res := leetcode.SpiralOrder(matrix)
	// fmt.Println(res)
	// intervals := [][]int{[]int{1, 4}, []int{2, 3}}
	// res := leetcode.Merge(intervals)
	// fmt.Println(res)
	// res := leetcode.SolveNQueens(4)
	// fmt.Println(res)
	res := leetcode.Rob([]int{1, 2, 3, 4, 3, 2, 1})
	fmt.Println(res)
}

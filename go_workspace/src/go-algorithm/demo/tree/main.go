package main

import (
	"fmt"
	"go-algorithm/leetcode"
	"go-algorithm/tree"
)

func main() {
	tr := tree.BuildTree([]int{0, 1, 2, 3, 4, 5, 6, 7, 8})
	tree.PrintTree(tr)
	res := leetcode.InorderTraversal(tr)
	fmt.Println(res)
	fmt.Println(1)
}

// +build ignore

package main

import (
	. "go-algorithm/tree"
)

/**
* Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
*/
func sumNumbers(root *TreeNode) int {
	var res int
	dfs(root, 0, &res)
	return res
}

func dfs(root *TreeNode, val int, res *int) {
	if root == nil {
		return
	}
	val = val*10 + root.Val
	if root.Left == nil && root.Right == nil {
		*res = *res + val
	}
	dfs(root.Left, val, res)
	dfs(root.Right, val, res)
}

func main() {

}

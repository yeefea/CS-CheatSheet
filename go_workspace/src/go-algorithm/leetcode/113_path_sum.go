// +build ignore

package main

/*
113. 路径总和 II
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
思路:回溯法,递归
*/
func pathSum(root *TreeNode, sum int) [][]int {
	res := make([][]int, 0)
	if root == nil {
		return res
	}
	stack := make([]int, 0)
	pathSumRecursive(root, sum, stack, &res)
	return res
}

func pathSumRecursive(root *TreeNode, sum int, stack []int, res *[][]int) {
	val := root.Val
	stack = append(stack, val)
	sum -= val
	if root.Left == nil && root.Right == nil {
		if sum == 0 {
			// append to res
			tmp := make([]int, len(stack))
			copy(tmp, stack)
			*res = append(*res, tmp)
		}
		return
	}

	// 回溯法
	if root.Left != nil {
		pathSumRecursive(root.Left, sum, stack, res)
	}
	if root.Right != nil {
		pathSumRecursive(root.Right, sum, stack, res)
	}
	stack = stack[:len(stack)-1]
}
func main() {

}

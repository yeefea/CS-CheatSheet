// +build ignore

package main

import (
	. "go-algorithm/tree"
)

/*
106. 从中序与后序遍历序列构造二叉树

根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]

返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

思路: 和105题类似
中序遍历 [left, mid, right]
后序遍历 [left, right, mid]
先用后序找到mid,用i表示
再找到mid在中序里的位置,分割出left和right,就可以知道left和right的长度
left的中序遍历是inorder[:i],后序遍历是postorder[:i]
left的后序遍历是inorder[i+1:],后序遍历是postorder[i:len(postorder)-1]
递归
*/

func buildTree(inorder []int, postorder []int) *TreeNode {
	if len(postorder) == 0 {
		return nil
	}
	root := new(TreeNode)
	root.Val = postorder[len(postorder)-1]
	var i int
	for ; i < len(inorder); i++ {
		if inorder[i] == root.Val {
			break
		}
	}
	root.Left = buildTree(inorder[:i], postorder[:i])
	root.Right = buildTree(inorder[i+1:], postorder[i:len(postorder)-1])
	return root
}

func main() {
}

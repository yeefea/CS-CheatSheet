// +build ignore

package main

import (
	. "go-algorithm/tree"
)

/*
105. 从前序与中序遍历序列构造二叉树
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]

返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
思路:先在preorder里找根节点,root=preorder[0]
在inorder里找到root的位置,用i表示
左子树的前序遍历是preorder[1:i+1],中序遍历是inorder[:i]
右子树的前序遍历是preorder[i+1:],中序遍历是inorder[i+1:]
递归构造
*/
func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 {
		return nil
	}
	root := &TreeNode{Val: preorder[0]}
	i := 0
	for ; i < len(inorder); i++ {
		if inorder[i] == root.Val {
			break
		}
	}
	root.Left = buildTree(preorder[1:i+1], inorder[:i])
	root.Right = buildTree(preorder[i+1:], inorder[i+1:])
	return root
}

func main() {

}

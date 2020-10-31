package tree

import "testing"

func TestTree(t *testing.T) {
	tree := &TreeNode{5, 5, nil, nil}
	tree.Describe()
	tree.Insert(0, 0)
	tree.Insert(10, 10)
	tree.Describe()

	tree.Insert(-1, 1)
	tree.Describe()
}

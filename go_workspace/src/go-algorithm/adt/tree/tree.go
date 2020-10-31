package tree

import (
	"fmt"
	"strings"
)

type TreeMap interface {
	Exists(int) bool
	Find(int) (interface{}, bool)
	FindMin() (int, interface{})
	FindMax() (int, interface{})
	Insert(int, interface{})
	Delete(int) (interface{}, bool)
}

// TreeNode binary search tree
type TreeNode struct {
	key   int
	value interface{}
	left  *TreeNode
	right *TreeNode
}

func (t *TreeNode) Describe() {
	stars := strings.Repeat("*", 10)
	fmt.Printf("%s %s %s\n", stars, "Tree", stars)
	t.describeNode(0)
	fmt.Println(strings.Repeat("*", 26))
}

func (t *TreeNode) describeNode(prefixLen int) {
	prefix := strings.Repeat(" ", prefixLen)
	fmt.Println(prefix, t.key)
	if t.left != nil {
		t.left.describeNode(prefixLen + 2)
	} else {
		t.printNil(prefixLen + 2)
	}
	if t.right != nil {
		t.right.describeNode(prefixLen + 2)
	} else {
		t.printNil(prefixLen + 2)
	}
}

func (t *TreeNode) printNil(prefixLen int) {
	fmt.Println(strings.Repeat(" ", prefixLen), "<nil>")
}

func (t *TreeNode) Insert(x int, val interface{}) {
	if x < t.key {
		t.insertLeft(x, val)
	} else if x > t.key {
		t.insertRight(x, val)
	} else {
		t.value = val
	}
}

func (t *TreeNode) insertLeft(x int, val interface{}) {
	if t.left == nil {
		t.left = &TreeNode{x, val, nil, nil}
	} else {
		t.left.Insert(x, val)
	}
}

func (t *TreeNode) insertRight(x int, val interface{}) {
	if t.right == nil {
		t.right = &TreeNode{x, val, nil, nil}
	} else {
		t.right.Insert(x, val)
	}
}
func (t *TreeNode) Find(x int) (interface{}, bool) {
	if x > t.right.key {
		if t.right == nil {
			return nil, false
		}
		return t.right.Find(x)
	}
	if x < t.left.key {
		if t.left == nil {
			return nil, false
		}
		return t.left.Find(x)
	}
	if t.right == nil {
		return nil, false
	}
	return t.value, true
}

func (t *TreeNode) FindMin() (int, interface{}) {
	if t.left == nil {
		return t.key, t.value
	}
	return t.left.FindMin()
}

func (t *TreeNode) FindMax() (int, interface{}) {
	if t.right == nil {
		return t.key, t.value
	}
	return t.right.FindMax()
}

/*
[1 2 3 4 ]
*/
// NewTreeFromLevelOrderSequence 从层序遍历列表生成二叉树
func NewTreeFromLevelOrderSequence(seq []interface{}) *TreeNode {
	if len(seq) == 0 {
		return nil
	}
	// 根节点
	root := &TreeNode{value: seq[0]}
	// 已经有了根节点,sequence里去掉第一个值
	seq = seq[1:]
	// 临时存放节点的队列
	queue := []*TreeNode{root}
	// 新的值添加到左子树
	isleft := true
	var cur, node *TreeNode
	for _, val := range seq {
		cur = queue[0]
		node = &TreeNode{value: val}
		if isleft {
			cur.left = node
		} else {
			cur.right = node
			queue = queue[1:]
		}
		queue = append(queue, node)
		// 翻转isleft
		isleft = !isleft
	}
	return root
}

// InorderTraversalRecursive 递归中序遍历
func InorderTraversalRecursive(tree *TreeNode) []interface{} {
	res := make([]interface{}, 0)
	inorderTraversalRec(tree, &res)
	return res
}

func inorderTraversalRec(tree *TreeNode, res *[]interface{}) {
	if tree == nil {
		return
	}
	inorderTraversalRec(tree.left, res)
	*res = append(*res, tree.value)
	inorderTraversalRec(tree.right, res)
}

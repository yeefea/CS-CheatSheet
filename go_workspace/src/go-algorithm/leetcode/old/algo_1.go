package leetcode

import (
	"fmt"
	"go-algorithm/tree"
	"go-algorithm/util"
)

/*
102. 二叉树层序遍历打印

给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
思路:队列+辅助变量
*/
func LevelOrder(root *tree.TreeNode) [][]int {
	res := make([][]int, 0)
	if root == nil {
		return res
	}
	res = append(res, make([]int, 0))
	q := []*tree.TreeNode{root}
	current, next := 1, 0
	for len(q) > 0 {
		current--
		tmp := q[0]
		lastLevel := &res[len(res)-1]
		*lastLevel = append(*lastLevel, tmp.Val)
		q = q[1:]
		if tmp.Left != nil {
			next++
			q = append(q, tmp.Left)
		}
		if tmp.Right != nil {
			next++
			q = append(q, tmp.Right)
		}
		if current == 0 {
			current = next
			next = 0
			res = append(res, make([]int, 0))
		}
	}
	return res[:len(res)-1]
}

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

Solution:
pre-order traversal: [root, [left], [right]]
in-order traversal: [[left], root, [right]]
1. find root node in pre-order array
2. find the index of root node in in-order array
3. find left and right
4. build recursively
*/
func BuildTree(preorder []int, inorder []int) *tree.TreeNode {
	if len(preorder) == 0 {
		return nil
	}
	root := &tree.TreeNode{Val: preorder[0]}
	i := 0
	for ; i < len(inorder); i++ {
		if inorder[i] == root.Val {
			break
		}
	}
	root.Left = BuildTree(preorder[1:i+1], inorder[:i])
	root.Right = BuildTree(preorder[i+1:], inorder[i+1:])
	return root
}

/*
114. 二叉树展开为链表
给定一个二叉树，原地将它展开为一个单链表。
例如，给定二叉树
    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
答案
可以发现展开的顺序其实就是二叉树的先序遍历。算法和 94 题中序遍历的 Morris 算法有些神似，我们需要两步完成这道题。
1.将左子树插入到右子树的地方
2.将原来的右子树接到左子树的最右边节点
3.考虑新的右子树的根节点，一直重复上边的过程，直到新的右子树为 null
*/
func Flatten(root *tree.TreeNode) {
	for root != nil {
		if root.Left != nil {
			tmp := root.Left
			for tmp.Right != nil {
				tmp = tmp.Right
			}
			tmp.Right = root.Right
			root.Right = root.Left
			root.Left = nil
		}
		root = root.Right
	}
}

/* 136. 只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
思路：位运算 bitwise xor
*/
func SingleNumber(nums []int) int {
	res := 0
	for _, x := range nums {
		res ^= x
	}
	return res
}

/*
139. 单词拆分
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

    拆分时可以重复使用字典中的单词。
    你可以假设字典中没有重复的单词。

示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。

示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

思路：动态规划
*/
func WordBreak(s string, wordDict []string) bool {
	if len(s) == 0 || len(wordDict) == 0 {
		return false
	}
	set := makeWordSet(wordDict)
	dp := make([]bool, len(s)+1) // 表示子串从0到i [0,i)可以拆分
	dp[0] = true                 // dp[0]表示空字符串可以被拆分
	for i := 1; i <= len(s); i++ {
		for j := 0; j < i; j++ {
			// dp[j]表示从0到j可以被拆分，s[j:i]表示从j到i，set[s[j:i]]查找字典中是否包含单词
			if _, found := set[s[j:i]]; dp[j] && found {
				dp[i] = true
				break
			}
		}
	}
	return dp[len(s)]
}

func makeWordSet(wordDict []string) map[string]struct{} {
	set := make(map[string]struct{}, len(wordDict))
	for _, w := range wordDict {
		set[w] = struct{}{}
	}
	return set
}

/*
142. 环形链表 II
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
说明：不允许修改给定的链表。

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：
输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：
输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。
进阶：
你是否可以不用额外空间解决此题？

思路:双指针
*/
func DetectCycle(head *ListNode) *ListNode {
	meet := getMeetPoint(head)
	if meet == nil {
		return nil
	}
	for head != meet {
		head = head.Next
		meet = meet.Next
	}
	return head
}

func getMeetPoint(head *ListNode) *ListNode {
	fast, slow := head, head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
		if fast == slow {
			return slow
		}
	}
	return nil
}

/*
146. LRU cache
*/
type LRUCache struct {
	capacity int
	size     int
	// store linked list entries
	cache map[int]*DListNode
	// linked list
	head *DListNode
	tail *DListNode
}

type DListNode struct {
	key  int
	val  int
	prev *DListNode
	next *DListNode
}

func newList() (*DListNode, *DListNode) {
	head := new(DListNode)
	tail := new(DListNode)
	// empty linked list
	head.next = tail
	tail.prev = head
	return head, tail
}

func Constructor(capacity int) LRUCache {
	head, tail := newList()
	cache := make(map[int]*DListNode, capacity)
	return LRUCache{capacity, 0, cache, head, tail}
}

func (this *LRUCache) Get(key int) int {
	if this.size == 0 {
		return -1
	}
	entry, ok := this.cache[key]
	if !ok {
		return -1
	}
	entry.prev.next = entry.next
	entry.next.prev = entry.prev
	entry.next = this.head.next
	entry.next.prev = entry
	this.head.next = entry
	entry.prev = this.head
	return entry.val
}

func (this *LRUCache) Put(key int, value int) {
	if this.capacity <= 0 {
		return
	}
	val := this.Get(key)
	if val != -1 {
		this.cache[key].val = value
		return
	}
	if this.size == this.capacity {
		entry := this.tail.prev
		entry.prev.next = entry.next
		entry.next.prev = entry.prev
		delete(this.cache, entry.key)
		this.size--
	}
	entry := &DListNode{key, value, this.head, this.head.next}
	this.cache[key] = entry
	this.head.next = entry
	entry.next.prev = entry
	this.size++
}

/*
148. 排序链表
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
示例 1:
输入: 4->2->1->3
输出: 1->2->3->4
示例 2:
输入: -1->5->3->4->0
输出: -1->0->3->4->5
解题思路:归并排序
自底向上比较麻烦，可以做到O(1)空间复杂度
递归是自顶向下的，可以做到O(logN)空间复杂度

todo:自底向上比较麻烦，临时变量很多，还要理一下思路
*/
func SortList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	h := head
	length := 0
	for h != nil {
		length++
		h = h.Next
	}
	res := new(ListNode)
	res.Next = head
	for interval := 1; interval < length; interval *= 2 {
		pre := res
		h = pre.Next
		for pre.Next != nil {
			h1 := h
			i := interval
			for h != nil && i > 0 {
				h = h.Next
				i--
			}
			if i > 0 {
				// h2 is empty
				break
			}
			h2 := h
			i = interval
			for h != nil && i > 0 {
				h = h.Next
				i--
			}
			// now h is the first node in next interval
			c1 := interval
			c2 := interval - i
			for c1 > 0 && c2 > 0 {
				if h1.Val < h2.Val {
					pre.Next = h1
					h1 = h1.Next
					c1--
				} else {
					pre.Next = h2
					h2 = h2.Next
					c2--
				}
				pre = pre.Next
			}
			if c1 > 0 {
				pre.Next = h1
			} else {
				pre.Next = h2
			}
			for c1 > 0 || c2 > 0 {
				pre = pre.Next
				c1--
				c2--
			}
			pre.Next = h // connect to the next interval
		}
	}
	return res.Next
}

func SortListRecursive(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	slow, fast := head, head.Next // fast=head.Next!!! fast要先走一格
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	mid := slow.Next
	slow.Next = nil

	left, right := SortListRecursive(head), SortListRecursive(mid)
	head = new(ListNode)
	tmp := head
	for left != nil && right != nil {
		if left.Val < right.Val {
			tmp.Next = left
			left = left.Next
		} else {
			tmp.Next = right
			right = right.Next
		}
		tmp = tmp.Next
	}
	if left == nil {
		tmp.Next = right
	} else {
		tmp.Next = left
	}
	return head.Next
}

/*
160. 相交链表
编写一个程序，找到两个单链表相交的起始节点。
Example 1.
	 4 -> 1 \
			 8 -> 4 -> 5 -> nil
5 -> 0 -> 1 /
return 8

Example 2.
2 -> 6 -> 1 -> nil
	 1 -> 5 -> nil
return nil
思路：双指针，非常巧妙！
创建两个指针 pA 和 pB，分别初始化为链表 A 和 B 的头结点。然后让它们向后逐结点遍历。
当 pA 到达链表的尾部时，将它重定位到链表 B 的头结点 (你没看错，就是链表 B);
类似的，当 pB 到达链表的尾部时，将它重定位到链表 A 的头结点。
若在某一时刻 pA 和 pB 相遇，则 pA/pB 为相交结点。
*/
func GetIntersectionNode(headA, headB *ListNode) *ListNode {
	if headA == nil || headB == nil {
		return nil
	}
	mp := make(map[int]int)
	fmt.Println(mp)
	var endA, endB *ListNode
	tmpA := headA
	tmpB := headB
	for endA == nil || endB == nil {
		if tmpA.Next == nil {
			endA = tmpA
			tmpA = headB
		} else {
			tmpA = tmpA.Next
		}
		if tmpB.Next == nil {
			endB = tmpB
			tmpB = headA
		} else {
			tmpB = tmpB.Next
		}
	}
	if endA != endB {
		return nil
	}
	for tmpA != tmpB {
		tmpA = tmpA.Next
		tmpB = tmpB.Next
	}
	return tmpA
}

/*
198. 打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
思路:动态规划
G[n] = max(G[n-1],nums[n]+G[n-2])
*/
func Rob(nums []int) int {
	if len(nums) == 0 {
		return 0
	} else if len(nums) == 1 {
		return nums[0]
	}
	g_i_2 := nums[0]                       // G[i-2]
	g_i_1 := util.MaxInt(nums[0], nums[1]) // G[i-1]
	for i := 2; i < len(nums); i++ {
		tmp := util.MaxInt(g_i_1, nums[i]+g_i_2) // max(G[i-1], nums[i]+G[i-2])
		g_i_2 = g_i_1
		g_i_1 = tmp
	}
	return g_i_1
}

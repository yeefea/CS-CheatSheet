package main

import (
	"fmt"
	"go-algorithm/list"

	"github.com/isdamir/gotype"
)

func createSampleNode(head *gotype.LNode, lst []int) {
	node := head
	for _, num := range lst {
		node.Next = &gotype.LNode{Data: num}
		node = node.Next
	}
}

func demoReverse() {
	head := &gotype.LNode{}
	gotype.CreateNode(head, 1)
	gotype.PrintNode("before:\t", head)
	list.RecursiveReverse(head)
	gotype.PrintNode("after:\t", head)
	head = &gotype.LNode{}
	gotype.CreateNode(head, 2)
	gotype.PrintNode("before:\t", head)
	list.RecursiveReverse(head)
	gotype.PrintNode("after:\t", head)
	head = &gotype.LNode{}
	gotype.CreateNode(head, 10)
	gotype.PrintNode("before:\t", head)
	list.RecursiveReverse(head)
	gotype.PrintNode("after:\t", head)

	head = &gotype.LNode{}
	gotype.CreateNode(head, 1)
	gotype.PrintNode("before:\t", head)
	list.InsertReverse(head)
	gotype.PrintNode("after:\t", head)
	head = &gotype.LNode{}
	gotype.CreateNode(head, 2)
	gotype.PrintNode("before:\t", head)
	list.InsertReverse(head)
	gotype.PrintNode("after:\t", head)
	head = &gotype.LNode{}
	gotype.CreateNode(head, 10)
	gotype.PrintNode("before:\t", head)
	list.InsertReverse(head)
	gotype.PrintNode("after:\t", head)

	var newNode *gotype.LNode
	head = &gotype.LNode{}
	gotype.CreateNode(head, 0)
	gotype.PrintNode("before:\t", head)
	newNode = list.ReverseHeadless(head.Next)
	head.Next = newNode
	gotype.PrintNode("headless:\t", head)

	head = &gotype.LNode{}
	gotype.CreateNode(head, 1)
	gotype.PrintNode("before:\t", head)
	newNode = list.ReverseHeadless(head.Next)
	head.Next = newNode
	gotype.PrintNode("headless:\t", head)

	head = &gotype.LNode{}
	gotype.CreateNode(head, 2)
	gotype.PrintNode("before:\t", head)
	newNode = list.ReverseHeadless(head.Next)
	head.Next = newNode
	gotype.PrintNode("headless:\t", head)

	head = &gotype.LNode{}
	gotype.CreateNode(head, 9)
	gotype.PrintNode("before:\t", head)
	newNode = list.ReverseHeadless(head.Next)
	head.Next = newNode
	gotype.PrintNode("headless:\t", head)

	head = &gotype.LNode{}
	gotype.CreateNode(head, 10)
	gotype.PrintNode("before:\t", head)
	newNode = list.ReverseHeadless(head.Next)
	head.Next = newNode
	gotype.PrintNode("headless:\t", head)
}

func demoRemoveDup() {
	head := &gotype.LNode{}
	lst := []int{1, 3, 1, 5, 5, 7, 6, 5, 4, 3, 2, 1}
	createSampleNode(head, lst)
	gotype.PrintNode("before remove:\t", head)
	list.RemoveDup(head)
	gotype.PrintNode("after remove:\t", head)

	head = &gotype.LNode{}
	createSampleNode(head, lst)
	gotype.PrintNode("before remove:\t", head)
	list.RemoveDupRecursive(head)
	gotype.PrintNode("after remove:\t", head)

	head = &gotype.LNode{}
	createSampleNode(head, lst)
	gotype.PrintNode("before remove:\t", head)
	list.RemoveDupHashSet(head)
	gotype.PrintNode("after remove:\t", head)

}

func demoAddList() {
	h1 := &gotype.LNode{}
	createSampleNode(h1, []int{3, 4, 5, 6, 7, 9})
	h2 := &gotype.LNode{}
	createSampleNode(h2, []int{9, 8, 2, 6, 5})
	gotype.PrintNode("h1:\t", h1)
	gotype.PrintNode("h2:\t", h2)
	res := list.Add(h1, h2)
	gotype.PrintNode("add:\t", res)

	h1 = &gotype.LNode{}
	createSampleNode(h1, []int{3, 4, 5, 6, 7, 8})
	h2 = &gotype.LNode{}
	createSampleNode(h2, []int{9, 8, 7, 6, 5})
	gotype.PrintNode("h1:\t", h1)
	gotype.PrintNode("h2:\t", h2)
	res = list.Add(h1, h2)
	gotype.PrintNode("add:\t", res)

}

func demoFindMiddle() {
	head := &gotype.LNode{}
	lst := []int{1, 3, 1, 5, 5, 7, 6, 5, 4, 3, 2, 1}
	createSampleNode(head, lst)
	mid := list.FindMiddleNode(head)
	fmt.Printf("middle node:\t%v\n", *mid)
}

func demoReorder() {
	var head *gotype.LNode
	head = &gotype.LNode{}
	gotype.CreateNode(head, 0)
	gotype.PrintNode("before:\t", head)
	list.Reorder(head)
	gotype.PrintNode("after:\t", head)
	head = &gotype.LNode{}
	gotype.CreateNode(head, 1)
	gotype.PrintNode("before:\t", head)
	list.Reorder(head)
	gotype.PrintNode("after:\t", head)
	head = &gotype.LNode{}
	gotype.CreateNode(head, 2)
	gotype.PrintNode("before:\t", head)
	list.Reorder(head)
	gotype.PrintNode("after:\t", head)
	head = &gotype.LNode{}
	gotype.CreateNode(head, 9)
	gotype.PrintNode("before:\t", head)
	list.Reorder(head)
	gotype.PrintNode("after:\t", head)
	head = &gotype.LNode{}
	gotype.CreateNode(head, 10)
	gotype.PrintNode("before:\t", head)
	list.Reorder(head)
	gotype.PrintNode("after:\t", head)
}

func demoLastK() {
	var head *gotype.LNode
	var lastK *gotype.LNode
	head = &gotype.LNode{}
	gotype.CreateNode(head, 10)
	gotype.PrintNode("before:\t", head)
	lastK = list.FindLastK(head, 1)
	fmt.Println("last k:\t", *lastK)
	lastK = list.FindLastK(head, 9)
	fmt.Println("last k:\t", *lastK)
	lastK = list.FindLastK(head, 10)
	fmt.Println("last k:\t", *lastK)
	fmt.Println()
	head = &gotype.LNode{}
	gotype.CreateNode(head, 2)
	gotype.PrintNode("before:\t", head)
	lastK = list.FindLastK(head, 3)
	fmt.Println("last k:\t", lastK)
	lastK = list.FindLastK(head, 2)
	fmt.Println("last k:\t", lastK)
	lastK = list.FindLastK(head, 1)
	fmt.Println("last k:\t", lastK)
}

func createSingleNode(num int) *gotype.LNode {
	return &gotype.LNode{Data: num}
}

func createLoopList() *gotype.LNode {
	head := &gotype.LNode{}
	ptr := head
	ptr.Next = createSingleNode(1)
	ptr.Next.Next = ptr
	return head
}

func createLoopList2() *gotype.LNode {
	head := &gotype.LNode{}
	gotype.CreateNode(head, 10)

	loopNode := head
	ptr := head
	for i := 0; i < 4; i++ {
		loopNode = loopNode.Next
	}
	for ptr.Next != nil {
		ptr = ptr.Next
	}
	ptr.Next = loopNode
	return head
}

func demoIsLoop() {
	var isLoop bool
	var head *gotype.LNode
	var loopNode *gotype.LNode

	head = &gotype.LNode{}
	gotype.CreateNode(head, 10)
	isLoop = list.IsLoop(head)
	fmt.Println("is loop:\t", isLoop)
	loopNode = list.FindLoopNode(head)
	fmt.Println("loop node:\t", loopNode)

	head = createLoopList()
	isLoop = list.IsLoop(head)
	fmt.Println("is loop:\t", isLoop)
	loopNode = list.FindLoopNode(head)
	fmt.Println("loop node:\t", loopNode)

	head = createLoopList2()
	isLoop = list.IsLoop(head)
	fmt.Println("is loop:\t", isLoop)
	loopNode = list.FindLoopNode(head)
	fmt.Println("loop node:\t", loopNode)
}

func demoSwapPair() {
	var head *gotype.LNode
	for i := 0; i < 10; i++ {
		head = &gotype.LNode{}
		gotype.CreateNode(head, i)
		gotype.PrintNode("before:\t", head)
		list.SwapPair(head)
		gotype.PrintNode("after:\t", head)
	}
}

func demoReverseKGroup() {
	head := &gotype.LNode{}
	gotype.CreateNode(head, 10)
	gotype.PrintNode("before:\t", head)
	list.ReverseKGroup(head, 3)
	gotype.PrintNode("after:\t", head)
}

func demoMerge() {
	head1 := &gotype.LNode{}
	head2 := &gotype.LNode{}
	gotype.CreateNode(head1, 10)
	gotype.CreateNode(head2, 9)
	res := list.Merge(head1, head2)
	gotype.PrintNode("after:\t", res)

}

func demoRemoveNode() {
	head := &gotype.LNode{}
	gotype.CreateNode(head, 5)
	gotype.PrintNode("before remove:\t", head)
	list.RemoveNode(head, head.Next.Next.Next) // remove 3
	gotype.PrintNode("after remove:\t", head)

	list.RemoveNode(head, head.Next.Next.Next) // remove 4
	gotype.PrintNode("after remove:\t", head)
	list.RemoveNode(head, head.Next) // remove 1
	gotype.PrintNode("after remove:\t", head)
	list.RemoveNode(head, head.Next) // remove 2
	gotype.PrintNode("after remove:\t", head)
	list.RemoveNode(head, head.Next) // remove nil
	gotype.PrintNode("after remove:\t", head)
}

func demoIsIntersect() {
	head1 := &gotype.LNode{}
	head2 := &gotype.LNode{}
	gotype.CreateNode(head1, 10)
	gotype.CreateNode(head2, 10)
	fmt.Println("is intersect:\t", list.IsIntersect(head1, head2))
	fmt.Println("intersect node:\t", list.FindIntersectNode(head1, head2))
	head1 = &gotype.LNode{}
	head2 = &gotype.LNode{}
	intersect := &gotype.LNode{Data: 1}
	head1.Next = &gotype.LNode{Data: 2}
	head1.Next.Next = intersect
	fmt.Println("is intersect:\t", list.IsIntersect(head1, head2))
	fmt.Println("intersect node:\t", list.FindIntersectNode(head1, head2))
	head2.Next = intersect
	fmt.Println("is intersect:\t", list.IsIntersect(head1, head2))
	fmt.Println("intersect node:\t", list.FindIntersectNode(head1, head2))

}

func newComplexLNode(num int) *list.ComplexLNode {
	return &list.ComplexLNode{Data: num}
}
func printComplexLNode(msg string, node *list.ComplexLNode) {

	if node == nil {
		fmt.Println(msg)
		return
	}
	fmt.Print(msg)
	for x := node; x != nil; x = x.Right {
		for y := x; y != nil; y = y.Down {
			fmt.Print(y.Data, " , ")
		}
		fmt.Print(" | ")
	}
	fmt.Println()
}

func getRange(start, stop, step int) []int {
	var lst []int
	for i := start; i < stop; i += step {
		lst = append(lst, i)
	}
	return lst
}

func demoFlatten() {
	head := newComplexLNode(0)
	curX := head
	for _, i := range getRange(5, 21, 5) {
		curY := curX
		for j := 0; j < 4; j++ {
			curY.Down = newComplexLNode(i + j - 4)
			curY = curY.Down
		}
		curX.Right = newComplexLNode(i)
		curX = curX.Right
	}
	printComplexLNode("before: ", head)
	list.Flatten(head)
	printComplexLNode("after: ", head)
}

func main() {
	// demoReverse()
	// demoRemoveDup()
	// demoAddList()
	// demoFindMiddle()
	// demoReorder()
	// demoLastK()
	// demoIsLoop()
	// demoSwapPair()
	// demoReverseKGroup()
	// demoMerge()
	// demoRemoveNode()
	demoIsIntersect()
	// demoFlatten()
}

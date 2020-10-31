package main

import (
	"fmt"
	"go-algorithm/stack"
)

func demoBuildStack() {
	stk := stack.NewLinkedStack()
	stack.PrintStack(stk)
	for i := 0; i < 5; i++ {
		stk.Push(i)
		stack.PrintStack(stk)
	}
	for i := 0; i < 5; i++ {
		stk.Pop()
		stack.PrintStack(stk)
	}

	stk = stack.NewSliceStack()
	stack.PrintStack(stk)
	for i := 0; i < 5; i++ {
		stk.Push(i)
		stack.PrintStack(stk)
	}
	for i := 0; i < 5; i++ {
		stk.Pop()
		stack.PrintStack(stk)
	}
}

func demoReverseStack() {
	stk := stack.NewLinkedStack()
	stack.PrintStack(stk)
	stack.ReverseStackRecursive(stk)
	stack.PrintStack(stk)

	for i := 0; i < 5; i++ {
		stk.Push(i)
	}
	stack.PrintStack(stk)
	stack.ReverseStackRecursive(stk)
	stack.PrintStack(stk)
	stack.ReverseStackRecursive(stk)
	stack.PrintStack(stk)

	for i := 5; i < 10; i++ {
		stk.Push(i)
	}
	stack.PrintStack(stk)
	stack.ReverseStackRecursive(stk)
	stack.PrintStack(stk)
}

func demoSortStack() {
	stk := stack.NewLinkedStack()
	stack.PrintStack(stk)
	stack.SortStack(stk)
	stack.PrintStack(stk)

	for i := 0; i < 5; i++ {
		stk.Push(i)
	}
	stack.PrintStack(stk)
	stack.SortStack(stk)
	stack.PrintStack(stk)

	for i := 6; i < 10; i++ {
		stk.Push(i)
	}
	stack.PrintStack(stk)
	stack.SortStack(stk)
	stack.PrintStack(stk)
}

func demoIsPopSerial() {
	pushList := []int{1, 2, 3, 4, 5}
	popList := []int{3, 2, 5, 4, 1}
	res := stack.IsPopSerial(pushList, popList)
	fmt.Println("is pop serial", res)
	popList = []int{5, 4, 3, 2, 1}
	res = stack.IsPopSerial(pushList, popList)
	fmt.Println("is pop serial", res)
	popList = []int{1, 2, 3, 4, 5}
	res = stack.IsPopSerial(pushList, popList)
	fmt.Println("is pop serial", res)
	popList = []int{3, 1, 2, 4, 5}
	res = stack.IsPopSerial(pushList, popList)
	fmt.Println("is pop serial", res)
}

func demoMinStack() {
	stk := stack.NewMinStack()
	stk.Push(1)
	stack.PrintStack(stk)
	fmt.Println("min:", stk.Min())

	stk.Push(2)
	stack.PrintStack(stk)
	fmt.Println("min:", stk.Min())

	stk.Push(3)
	stack.PrintStack(stk)
	fmt.Println("min:", stk.Min())

	stk.Push(0)
	stack.PrintStack(stk)
	fmt.Println("min:", stk.Min())

	stk.Push(-1)
	stack.PrintStack(stk)
	fmt.Println("min:", stk.Min())

	stk.Push(4)
	stack.PrintStack(stk)
	fmt.Println("min:", stk.Min())

	stk.Pop()
	stack.PrintStack(stk)
	fmt.Println("min:", stk.Min())

	stk.Pop()
	stack.PrintStack(stk)
	fmt.Println("min:", stk.Min())
	stk.Pop()
	stack.PrintStack(stk)
	fmt.Println("min:", stk.Min())
	stk.Pop()
	stack.PrintStack(stk)
	fmt.Println("min:", stk.Min())
	stk.Pop()
	stack.PrintStack(stk)
	fmt.Println("min:", stk.Min())
	stk.Pop()
	stack.PrintStack(stk)
}

func demoStackQueue() {
	q := stack.NewStackQueue()
	q.PushRight(1)
	stack.PrintStackQueue(q)
	q.PushRight(2)
	q.PushRight(3)
	q.PopLeft()
	q.PushRight(4)
	q.PopLeft()
	q.PushRight(5)
	q.PushRight(6)
	q.PopLeft()
	stack.PrintStackQueue(q)

}

func main() {
	// demoBuildStack()
	// demoReverseStack()
	// demoSortStack()
	// demoIsPopSerial()
	// demoMinStack()
	demoStackQueue()
}

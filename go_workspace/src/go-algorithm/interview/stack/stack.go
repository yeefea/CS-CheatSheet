package stack

import (
	"fmt"

	"github.com/isdamir/gotype"
)

// Stack interface of stack data structure
type Stack interface {
	Push(int)
	Pop() int
	GetSize() int
	IsEmpty() bool
	Top() int
}

// NewSliceStack stack implemented by slice
func NewSliceStack() Stack {
	return &SliceStack{}
}

// NewLinkedStack stack implemented by linked list
func NewLinkedStack() Stack {
	return &LinkedStack{head: &gotype.LNode{}}
}

// NewMinStack stack with min value
func NewMinStack() *MinStack {
	return &MinStack{datastack: NewLinkedStack(), minStack: NewLinkedStack()}
}

// LinkedStack linked stack
type LinkedStack struct {
	head *gotype.LNode
	size int
}

// Push push element
func (stack *LinkedStack) Push(n int) {
	tmp := stack.head.Next
	stack.size++
	stack.head.Next = &gotype.LNode{Data: n, Next: tmp}
}

// Pop pop element
func (stack *LinkedStack) Pop() int {
	tmp := stack.head.Next
	stack.head.Next = tmp.Next
	stack.size--
	return tmp.Data.(int)
}

// GetSize get stack size
func (stack *LinkedStack) GetSize() int {
	return stack.size
}

// IsEmpty stack is empty
func (stack *LinkedStack) IsEmpty() bool {
	return stack.size == 0
}

// Top top element
func (stack *LinkedStack) Top() int {
	return stack.head.Next.Data.(int)
}

// Print print stack
func (stack *LinkedStack) Print() {
	fmt.Printf("top [")
	if stack.head.Next == nil {
		fmt.Println("]")
		return
	}
	tmp := stack.head.Next
	for tmp.Next != nil {
		fmt.Printf("%d ", tmp.Data.(int))
		tmp = tmp.Next
	}
	if tmp != nil {
		fmt.Printf("%d", tmp.Data.(int))
	}
	fmt.Println("]")
}

// SliceStack stack
type SliceStack struct {
	arr  []int
	size int
}

// GetSize get stack size
func (stack *SliceStack) GetSize() int {
	return stack.size
}

// IsEmpty stack is empty
func (stack *SliceStack) IsEmpty() bool {
	return stack.size == 0
}

// Top get the top element
func (stack *SliceStack) Top() int {
	return stack.arr[stack.size-1]
}

// Pop pop element from stack
func (stack *SliceStack) Pop() int {
	res := stack.arr[stack.size-1]
	stack.arr = stack.arr[:stack.size-1]
	stack.size--
	return res
}

// Push push element to stack
func (stack *SliceStack) Push(n int) {
	stack.size++
	stack.arr = append(stack.arr, n)
}

// Print print stack
func (stack *SliceStack) Print() {
	fmt.Println(stack.arr, "top")
}

// MinStack stack with Min() function
type MinStack struct {
	datastack Stack
	minStack  Stack
}

// Push push element
func (stack *MinStack) Push(n int) {
	stack.datastack.Push(n)
	if stack.minStack.IsEmpty() || n <= stack.minStack.Top() {
		stack.minStack.Push(n)
	}
}

// Pop pop element
func (stack *MinStack) Pop() int {
	res := stack.datastack.Pop()
	if res == stack.minStack.Top() {
		stack.minStack.Pop()
	}
	return res
}

// Min get min value in stack
func (stack *MinStack) Min() int {
	return stack.minStack.Top()
}

// Top get top value
func (stack *MinStack) Top() int {
	return stack.datastack.Top()
}

// GetSize get stack size
func (stack *MinStack) GetSize() int {
	return stack.datastack.GetSize()
}

// IsEmpty stack is empty
func (stack *MinStack) IsEmpty() bool {
	return stack.datastack.IsEmpty()
}

// PrintStack print stack
func PrintStack(stack Stack) {
	if stack.IsEmpty() {
		fmt.Println("[]")
		return
	}
	fmt.Printf("[")
	printStackRecursive(stack)
	fmt.Println("]")
}

func printStackRecursive(stack Stack) {
	if stack.GetSize() == 1 {
		fmt.Printf("%d", stack.Top())
		return
	}
	data := stack.Pop()
	fmt.Printf("%d ", data)
	printStackRecursive(stack)
	stack.Push(data)
}

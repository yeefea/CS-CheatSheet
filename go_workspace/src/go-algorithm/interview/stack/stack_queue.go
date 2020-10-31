package stack

import "fmt"

// StackQueue FIFO queue implemented by stack
type StackQueue struct {
	pushStack Stack
	popStack  Stack
}

// NewStackQueue construct new stack queue
func NewStackQueue() *StackQueue {
	return &StackQueue{NewLinkedStack(), NewLinkedStack()}
}

// Push add element to the end of queue
func (sq *StackQueue) PushRight(n int) {
	sq.pushStack.Push(n)
}

// Pop pop first element
func (sq *StackQueue) PopLeft() int {
	if sq.popStack.IsEmpty() {
		for !sq.pushStack.IsEmpty() {
			sq.popStack.Push(sq.pushStack.Pop())
		}
	}
	return sq.popStack.Pop()
}

// GetSize return queue size
func (sq *StackQueue) GetSize() int {
	return sq.pushStack.GetSize() + sq.popStack.GetSize()
}

// Top first element in queue
func (sq *StackQueue) Top() int {
	if sq.popStack.IsEmpty() {
		for !sq.pushStack.IsEmpty() {
			sq.popStack.Push(sq.pushStack.Pop())
		}
	}
	return sq.popStack.Top()

}

// IsEmpty queue is empty
func (sq *StackQueue) IsEmpty() bool {
	return sq.pushStack.IsEmpty() && sq.popStack.IsEmpty()
}

// PrintStackQueue print stack queue
func PrintStackQueue(sq *StackQueue) {
	if sq.IsEmpty() {
		fmt.Println("[]")
		return
	}
	if sq.GetSize() == 1 {
		fmt.Printf("[%d]\n", sq.Top())
		return
	}
	fmt.Printf("[")
	var tmp int
	for i := 0; i < sq.GetSize()-1; i++ {
		tmp = sq.PopLeft()
		sq.PushRight(tmp)
		fmt.Printf("%d ", tmp)
	}
	tmp = sq.PopLeft()
	sq.PushRight(tmp)
	fmt.Printf("%d]\n", tmp)
}

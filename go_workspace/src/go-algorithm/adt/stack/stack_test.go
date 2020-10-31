package stack

import (
	"testing"
)

func TestNewStack(t *testing.T) {
	stk := NewStack()
	stk.Pop()
	stk.Describe()
	stk.Push(1)
	stk.Describe()
	stk.Push(2)
	stk.Describe()
	stk.Push(3)
	stk.Describe()
	stk.Push(4)
	stk.Describe()
	stk.Pop()
	stk.Describe()
	stk.Pop()
	stk.Describe()
	stk.Pop()
	stk.Describe()
	stk.Push(5)
	stk.Describe()
	stk.Push(6)
	stk.Describe()
	stk.Push(7)
	stk.Describe()
	stk.Pop()
	stk.Describe()
}

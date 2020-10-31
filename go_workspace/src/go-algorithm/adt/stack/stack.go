package stack

import (
	"go-algorithm/adt/list"
)

type Stack struct {
	lst *list.DoubleList
}

func NewStack() *Stack {
	lst := list.NewDoubleList()
	return &Stack{lst}
}

func (stk *Stack) Size() int {
	return stk.lst.Size()
}
func (stk *Stack) Push(val interface{}) {
	stk.lst.PushFront(val)
}

func (stk *Stack) Pop() (interface{}, bool) {
	return stk.lst.PopFront()
}

func (stk *Stack) Describe() {
	stk.lst.Describe()
}

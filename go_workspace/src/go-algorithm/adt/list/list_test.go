package list

import (
	"testing"
)

func TestNewList(t *testing.T) {
	lst := NewDoubleList()
	lst.PushBack(1)
	lst.PushBack(2)
	lst.PushBack(3)
	lst.PushBack(4)
	lst.Describe()
	lst.PopBack()
	lst.Describe()
	lst.PopBack()
	lst.Describe()
	lst.PopBack()
	lst.Describe()
	lst.PopBack()
	lst.Describe()
	lst.PopBack()
	lst.Describe()
	lst.PopBack()
	lst.Describe()
	lst.PopBack()
	lst.Describe()

	lst.PushBack(3)
	lst.PushBack(4)
	lst.Describe()
}

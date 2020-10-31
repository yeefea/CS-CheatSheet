package queue

import (
	"go-algorithm/adt/list"
)

type Queue interface {
	Size() int
	PushBack(interface{})
	PopFront() (interface{}, bool)
	Describe()
}

func NewQueue() Queue {
	return list.NewDoubleList()
}

package queue

import (
	"testing"
)

func TestNewStack(t *testing.T) {
	q := NewQueue()
	q.Describe()
	q.PopFront()
	q.Describe()
	q.PushBack(1)
	q.Describe()
	q.PushBack(2)
	q.Describe()
	q.PushBack(3)
	q.Describe()
	q.PopFront()
	q.Describe()
	q.PopFront()
	q.Describe()
	q.PushBack(4)
	q.Describe()
	q.PushBack(5)
	q.Describe()
	q.PushBack(6)
	q.Describe()
	q.PopFront()
	q.Describe()
	q.PopFront()
	q.Describe()
}

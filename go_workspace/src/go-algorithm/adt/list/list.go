package list

import (
	"fmt"
)

type DoubleListNode struct {
	Value interface{}
	prev  *DoubleListNode
	next  *DoubleListNode
}

type DoubleList struct {
	head DoubleListNode
	tail DoubleListNode
	size int
}

func NewDoubleList() *DoubleList {
	lst := DoubleList{}
	lst.head.next = &lst.tail
	lst.tail.prev = &lst.head
	return &lst
}

func NewListFromSlice(arr []interface{}) *DoubleList {
	lst := NewDoubleList()
	for _, x := range arr {
		lst.PushBack(x)
	}
	return lst
}

func (lst *DoubleList) Size() int {
	return lst.size
}

func (lst *DoubleList) PushFront(val interface{}) {
	head := &lst.head
	next := head.next
	node := DoubleListNode{Value: val, prev: head, next: next}
	head.next = &node
	next.prev = &node
	lst.size++
}

func (lst *DoubleList) PushBack(val interface{}) {
	tail := &lst.tail
	prev := tail.prev
	node := DoubleListNode{Value: val, prev: prev, next: tail}
	prev.next = &node
	tail.prev = &node
	lst.size++
}

func (lst *DoubleList) PopFront() (interface{}, bool) {
	if lst.size == 0 {
		return nil, false
	}
	lst.size--
	res := lst.head.next
	res.next.prev = &lst.head
	lst.head.next = res.next
	res.prev = nil
	res.next = nil
	return res.Value, true
}

// PopBack return value, ok
func (lst *DoubleList) PopBack() (interface{}, bool) {
	if lst.size == 0 {
		return nil, false
	}
	lst.size--
	res := lst.tail.prev
	res.prev.next = &lst.tail
	lst.tail.prev = res.prev
	res.prev = nil
	res.next = nil
	return res.Value, true
}

func (lst *DoubleList) Describe() {
	cur := lst.head.next
	fmt.Printf("size: %d [ ", lst.size)
	for cur != &lst.tail {
		fmt.Printf("%v ", cur.Value)
		cur = cur.next
	}
	fmt.Printf("]\n")
}

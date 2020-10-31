package main

import (
	"fmt"
	"go-algorithm/adt/list"
)

type Element struct {
	next, prev *Element
	Value      interface{}
}

func main() {
	sli := []interface{}{1, 2, 3, 4, 5}
	lst := list.NewListFromSlice(sli)
	for x := lst.Front(); x != nil; x = x.Next() {
		fmt.Printf("%v ", x.Value)
	}
	fmt.Println()

	ele := new(Element)
	ele.next = ele
	ele.prev = ele
	fmt.Println(ele)
}

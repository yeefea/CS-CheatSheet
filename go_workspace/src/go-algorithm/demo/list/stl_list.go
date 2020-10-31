// +build ignore

package main

import (
	"container/list"
	"fmt"
)

func main() {
	l := list.New()

	el := l.PushBack(1)
	fmt.Println(el)
}

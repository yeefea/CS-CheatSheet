// +build ignore

package main

import (
	"fmt"
	"go-algorithm/adt/disjset"
)

func main() {
	size := 10
	set := disjset.NewDisjSet(size)
	set.SetUnion(4, 5)
	set.SetUnion(6, 7)
	set.SetUnion(4, 6)
	set.SetUnion(3, 4)
	set.SetUnion(2, 4)
	for i := 0; i < len(set); i++ {
		fmt.Println(set.Find(i))
	}
}

package main

import (
	"fmt"
	"sort"
)

func main() {
	nums := []int{1, 2, 3, 4, 5}
	sort.Ints(nums)
	sort.Reverse()
	fmt.Println(nums)
}

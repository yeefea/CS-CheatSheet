// +build ignore

package main

import (
	"fmt"
	"sort"
)

func main() {
	res := naiveSubSets([]int{1, 2, 2}) // 会重复
	fmt.Println(res)
	res = SubsetsWithDup([]int{1, 2, 2}) // 不会重复
	fmt.Println(res)
}

func naiveSubSets(nums []int) [][]int {
	res := make([][]int, 0)
	if len(nums) == 0 {
		return res
	}
	sort.Ints(nums) // 先排序!!!
	prefix := make([]int, 0)
	naiveBacktrack(prefix, 0, nums, &res)
	return res
}

func naiveBacktrack(prefix []int, index int, nums []int, res *[][]int) {
	tmp := make([]int, len(prefix))
	copy(tmp, prefix) // copy
	*res = append(*res, tmp)
	if index == len(nums) {
		return
	}
	prefix = append(prefix, nums[index])
	backtrack(prefix, index+1, nums, res)
	prefix = prefix[:len(prefix)-1]
	for i := index + 1; i < len(nums); i++ {
		prefix = append(prefix, nums[i])
		backtrack(prefix, i+1, nums, res)
		prefix = prefix[:len(prefix)-1]
	}
}

// SubsetsWithDup 90. subsets with duplications
func SubsetsWithDup(nums []int) [][]int {
	res := make([][]int, 0)
	if len(nums) == 0 {
		return res
	}
	sort.Ints(nums) // 先排序!!!
	prefix := make([]int, 0)
	backtrack(prefix, 0, nums, &res)
	return res
}

func backtrack(prefix []int, index int, nums []int, res *[][]int) {
	tmp := make([]int, len(prefix))
	copy(tmp, prefix) // copy
	*res = append(*res, tmp)
	if index == len(nums) {
		return
	}
	prefix = append(prefix, nums[index])
	backtrack(prefix, index+1, nums, res)
	prefix = prefix[:len(prefix)-1]
	for i := index + 1; i < len(nums); i++ {
		// 这里是和naive唯一不同的地方，如果数字相同，需要跳过去重
		if nums[i] == nums[i-1] {
			// remove duplicated number
			continue
		}
		prefix = append(prefix, nums[i])
		backtrack(prefix, i+1, nums, res)
		prefix = prefix[:len(prefix)-1]
	}
}

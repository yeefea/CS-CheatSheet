// +build ignore

package main

import (
	"fmt"
)

func main() {
	sets := subsets([]int{1, 2, 3, 4, 5})
	for _, x := range sets {
		fmt.Println(x)
	}

}

func subsets(nums []int) [][]int {
	// 保存最终结果
	result := make([][]int, 0)
	// 保存中间结果
	list := make([]int, 0)
	backtrack(nums, 0, list, &result)
	return result
}

// nums 给定的集合
// pos 下次添加到集合中的元素位置索引
// list 临时结果集合(每次需要复制保存)
// result 最终结果
func backtrack(nums []int, pos int, list []int, result *[][]int) {
	// 把临时结果复制出来保存到最终结果
	ans := make([]int, len(list))
	// copy
	copy(ans, list)
	*result = append(*result, ans)
	// 选择、处理结果、再撤销选择
	for i := pos; i < len(nums); i++ {
		// list追加一个数
		list = append(list, nums[i])
		// 回溯
		backtrack(nums, i+1, list, result)
		// list去掉最后一个数
		list = list[0 : len(list)-1]
	}
}

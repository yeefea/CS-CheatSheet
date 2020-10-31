// +build ignore

package main

import (
	"fmt"
)

/*
快速排序
*/
func main() {
	proto := []int{1, 4, 3, 2, 6, 5, 9, 7, 8}
	nums := make([]int, len(proto))

	// DemoQuickSort
	copy(nums, proto)
	fmt.Println("before sort", nums)
	QuickSort(nums)
	fmt.Println("after sort", nums)

	// DemoQuickSelect
	for i := 1; i <= len(nums); i++ {
		copy(nums, proto)
		res := QuickSelect(nums, i)
		fmt.Printf("quick select i=%d, num=%d\n", i, res)
	}
	// this will panic
	// res := QuickSelect(nums, len(nums)+1)
	// fmt.Println(res)
}

// QuickSort快速排序
func QuickSort(nums []int) {
	quickSort(nums, 0, len(nums))
}

func quickSort(nums []int, begin, end int) {
	// 处理[begin, end)前闭后开区间
	if begin >= end {
		return
	}
	pivot := partition(nums, begin, end)
	quickSort(nums, begin, pivot)
	// pivot已经在正确的位置上,不用处理了
	// 所以这里用pivot+1
	quickSort(nums, pivot+1, end)
}

func partition(nums []int, begin, end int) int {
	last := end - 1
	// [begin, end)最后一个元素作为pivot
	pivot := nums[last]
	// i指向第一个元素
	i := begin
	// j遍历第一个到倒数第二个元素 j走得比i快
	// 在i左边的都是**小于等于**pivot的数
	// 在i右边,j左边的都是**大于**pivot的数
	for j := begin; j < last; j++ {
		// 发现nums[j]比较小 则交换i j指向的元素
		// i,j一起向前走一格
		if nums[j] <= pivot {
			// 交换i j指向的元素 nums[i] <-> nums[j]
			nums[i], nums[j] = nums[j], nums[i]
			// i 指向下一个元素
			i++
		}
		// nums[j]较大则j继续往前走一格, i不动保持指向较大的元素
	}
	// 把pivot元素放到中间
	nums[i], nums[last] = nums[last], nums[i]
	return i
}

// QuickSelect 快速选择算法 O(N)
func QuickSelect(nums []int, k int) int {
	if len(nums) == 0 || k > len(nums) {
		panic(fmt.Sprintf("k is larger than the total length of array (k=%d, length=%d)", k, len(nums)))
	}
	k--
	left, right := 0, len(nums)
	for {
		pivot := partition(nums, left, right)
		if k < pivot {
			right = pivot
		} else if k > pivot {
			left = pivot + 1
		} else {
			return nums[pivot]
		}
	}
}

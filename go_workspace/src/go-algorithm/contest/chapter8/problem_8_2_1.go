// +build ignore

package main

import (
	"fmt"
)

/*
归并排序
顺便可以计算逆序对的数量
*/

func main() {
	DemoMergeSort()
	DemoReversePairs()
}

func DemoMergeSort() {
	nums := []int{5, 4, 1, 2, 1, 3}
	MergeSort(nums)
	fmt.Println(nums)
}

func DemoReversePairs() {
	nums := []int{5, 4, 3, 2, 1}
	res := ReversePairs(nums)
	fmt.Println("reverse pairs", res)

}

// MergeSort 归并排序 时间复杂度O(NlogN) 空间复杂度O(N)
func MergeSort(nums []int) {
	if len(nums) < 2 {
		return
	}
	mergeSort(nums, 0, len(nums))
}

func mergeSort(nums []int, begin, end int) {
	if end-begin < 2 {
		return
	}
	mid := begin + (end-begin)/2
	mergeSort(nums, begin, mid)
	mergeSort(nums, mid, end)
	tmp := make([]int, end-begin)
	idx := 0
	left, right := begin, mid
	// 这样写比书上的逻辑清晰!
	// left right指针只要有一个超出边界则停止循环
	for ;left < mid && right < end; idx++{
		if nums[left] <= nums[right]{
			tmp[idx] = nums[left]
			left++
		}else{
			tmp[idx] = nums[right]
			right++
		}
	}
	for left < mid{
		tmp[idx] = nums[left]
		idx++
		left++
	}
	for right < end{
		tmp[idx] = nums[right]
		idx++
		right++
	}
	fmt.Println(nums)
	copy(nums[begin:end], tmp)
}

// ReversePairs 逆序对
func ReversePairs(nums []int) int {
	return MergeSortReversePairs(nums)
}

// MergeSortReversePairs 归并排序顺便计算逆序对的数量
func MergeSortReversePairs(nums []int) int {
	return mergeSortReversePairs(nums, 0, len(nums))
}

func mergeSortReversePairs(nums []int, begin, end int) int {
	if end-begin < 2 {
		return 0
	}
	mid := begin + (end-begin)/2
	cnt := mergeSortReversePairs(nums, begin, mid) + mergeSortReversePairs(nums, mid, end)
	tmp := make([]int, end-begin)
	idx := 0
	left, right := begin, mid
	// 这样写比书上的逻辑清晰!
	// left right指针只要有一个超出边界则停止循环
	for ;left < mid && right < end; idx++{
		if nums[left] <= nums[right]{
			tmp[idx] = nums[left]
			left++
		}else{
			tmp[idx] = nums[right]
			right++
			// 合并操作是从小到大进行的
			// 当右边的一个数复制到tmp中时
			// 左边还没来得及复制到tmp中的那些数就是逆序对
			cnt += mid-left
		}
	}
	for left < mid{
		// 这里是复制left,不存在新的逆序对
		tmp[idx] = nums[left]
		idx++
		left++
	}
	for right < end{
		// 这里是复制right
		// 由于mid-left=0
		// 也不存在新的逆序对
		tmp[idx] = nums[right]
		idx++
		right++
	}
	copy(nums[begin:end], tmp)
	return cnt
}

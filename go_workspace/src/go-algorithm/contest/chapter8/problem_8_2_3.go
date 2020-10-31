// +build ignore

package main

import "fmt"

func main() {
	demoBisectSearch()
	demoLowerBound()
	demoUpperBound()

}

func demoBisectSearch() {
	nums := []int{1, 2, 3, 4, 5, 7, 8, 9, 10}
	var res int
	for i := 0; i < 12; i++ {
		res = BisectSearch(nums, i)
		fmt.Println(i, res)
	}
}

func demoLowerBound() {
	nums := []int{1, 2, 3, 4, 5, 5, 5, 5, 7, 8, 9, 10}
	var res int
	for i := 0; i < 12; i++ {
		res = LowerBound(nums, i)
		fmt.Println(i, res)
	}
}

func demoUpperBound() {
	nums := []int{1, 2, 3, 4, 5, 5, 5, 5, 7, 8, 9, 10}
	var res int
	for i := 0; i < 12; i++ {
		res = UpperBound(nums, i)
		fmt.Println(i, res)
	}
}

// BisectSearch 二分查找法
func BisectSearch(nums []int, v int) int {
	// [] len=0 -> -1
	// [0] len=1 -> 0+1/2 -> 0
	// [0,1] len=2 -> 1 0+2/2 -> 1
	// [0,1,2] len=3 -> 0+3/2 -> 1
	// [0,1,2,3] len=4 -> 2 0+4/2 -> 2
	// [left,right) 左闭右开区间
	left, mid, right := 0, 0, len(nums)
	for left < right {
		mid = left + (right-left)/2 // 向零取整，当数组长度为偶数时，mid指向中间元素或偏右一个元素
		if nums[mid] == v {
			return mid
		} else if nums[mid] > v {
			right = mid // 右边是开区间
		} else {
			left = mid + 1 // 左边是闭区间
		}
	}
	return -1
}

// LowerBound 当元素有重复时返回最左位置，当元素不存在时返回可以插入该值的位置
func LowerBound(nums []int, v int) int {
	// [] len=0 -> -1
	// [0] len=1 -> 0+1/2 -> mid=0
	// [0,1] len=2 -> 1 0+2/2 -> mid=1 当元素个数为偶数时，中点是右偏的，指向中间偏右的元素
	// [0,1,2] len=3 -> 0+3/2 -> mid=1 当元素个数为奇数时，中点在正中间
	// [0,1,2,3] len=4 -> 2 0+4/2 -> mid=2
	// [left,right) 左闭右开区间
	left, mid, right := 0, 0, len(nums)
	for left < right {
		mid = left + (right-left)/2
		if nums[mid] < v {
			left = mid + 1
		} else { // nums[mid] >= v
			right = mid
		}
	}
	return left
}

func UpperBound(nums []int, v int) int {
	left, mid, right := 0, 0, len(nums)
	for left < right {
		mid = left + (right-left)/2
		if nums[mid] <= v {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return left
}

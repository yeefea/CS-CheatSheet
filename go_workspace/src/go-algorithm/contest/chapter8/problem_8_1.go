// +build ignore

package main

import (
	"fmt"
	"go-algorithm/util"
)

/*
最大连续和问题
*/
func main() {
	nums := []int{1, 2, 3}
	res := brutalForce(nums)
	fmt.Println(res)
	res = cachedPrefix(nums)
	fmt.Println(res)
	res = divideAndConquer(nums)
	fmt.Println(res)
	res = cachedPrefixFast(nums)
	fmt.Println(res)
}

// brutalForce 暴力枚举法 复杂度O(N^3) 三层嵌套循环
func brutalForce(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	best := nums[0]
	for i := 0; i < len(nums); i++ {
		for j := i; j < len(nums); j++ {
			// sum表示num[i,...j-1]的和
			sum := 0
			// 求和
			for k := i; k <= j; k++ {
				sum += nums[k]
			}
			// 更新最大值
			best = util.MaxInt(sum, best)
		}
	}
	return best
}

// cachedPrefix 缓存数组前缀的和 复杂度O(N^2) 两层嵌套循环
func cachedPrefix(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	sums := make([]int, len(nums))
	sums[0] = nums[0]
	// 记录最大连续和
	best := nums[0]
	// 累积求和
	// sums[i]表示nums[0,...,i]的和
	for i := 1; i < len(nums); i++ {
		sums[i] = sums[i-1] + nums[i]
		best = util.MaxInt(best, sums[i])
	}
	for i := 1; i < len(nums); i++ {
		for j := i; j < len(nums); j++ {
			// sum表示nums[i,...,j]的和,可以用sums[j] - sums[i-1]计算
			var sum int
			sum = sums[j] - sums[i-1]
			// 更新最大值
			best = util.MaxInt(sum, best)
		}
	}
	return best
}

// divideAndConquer 分制法
func divideAndConquer(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	// here length of nums >= 1
	return maxSum(nums, 0, len(nums))
}

/*
分治法 O(NlogN)复杂度
把数组划分成左右两个子数组 left = [begin, mid), right = [mid, end)
每次分割,最大序列和有**三种**情况
	可能在左边
	可能在右边
	可能跨越中间
要取三者的最大值
*/
// maxSum max sum in range [begin, end)
func maxSum(nums []int, begin, end int) int {
	// 比如0, 1 直接返回
	if end-begin == 1 {
		return nums[begin]
	}
	// here length of nums >=2
	mid := begin + (end-begin)/2 // 比如0, 2 => mid=1 ; 0, 3 => mid = 1 ; 0,4 => mid = 2
	left, right := maxSum(nums, begin, mid), maxSum(nums, mid, end)
	// 左右两边的较大值
	max := util.MaxInt(left, right)
	// 重复使用left, right
	left, right = 0, 0
	// 从右向左 求左半部分最大序列和 i--
	tmp := 0
	for i := mid - 1; i >= begin; i-- {
		tmp += nums[i]
		left = util.MaxInt(tmp, left)
	}
	// 从左向右 求右半部分最大序列和 i++
	tmp = 0
	for i := mid; i < end; i++ {
		tmp += nums[i]
		right = util.MaxInt(tmp, right)
	}
	return util.MaxInt(max, left+right)
}

/*
优化后的cachedPrefix
当j确定时,sums[j]-sum[i-1]最大 <=> sums[i-1]最小
只需记录sums出现过的最小值即可
*/
// cachedPrefixFast O(N)复杂度
func cachedPrefixFast(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	// sum表示nums[0,...,j]的和
	sum := 0
	// tmpMin表示之前出现过的sum的最小值
	tmpMin := 0
	// 记录最大连续和
	best := nums[0]

	for j := 0; j < len(nums); j++ {
		// nums[0,...,j]求和
		sum += nums[j]
		// sum - 之前出现过的最小sum
		best = util.MaxInt(best, sum-tmpMin)
		// 更新目前出现过的最小sum
		tmpMin = util.MinInt(tmpMin, sum)
	}
	return best
}

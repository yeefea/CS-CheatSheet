package leetcode

/*
剑指offer
*/

/*
51. 数组中的逆序对
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
示例 1:
输入: [7,5,6,4]
输出: 5
限制：0 <= 数组长度 <= 50000
*/
func ReversePairs(nums []int) int {
	return mergeSort(nums, 0, len(nums)-1)
}
func mergeSort(nums []int, left, right int) int {
	// [left, right] inclusive on both sides
	if left >= right {
		return 0
	}
	// better than (left+right)/2
	mid := left + (right-left)/2 // left bias
	cnt := mergeSort(nums, left, mid) + mergeSort(nums, mid+1, right)
	tmp := []int{}
	l, r := left, mid+1
	for l < mid+1 && r <= right {
		// 前面一个数字大于后面的数字，如果前面的数字x等于后面的数字y，前面这个数字的逆序对贡献还是要加上的，这里小于等于号**很重要** <= important!
		if nums[l] <= nums[r] {
			tmp = append(tmp, nums[l])
			cnt += r - mid - 1
			l++
		} else {
			tmp = append(tmp, nums[r])
			r++
		}
	}
	for ; l < mid+1; l++ {
		tmp = append(tmp, nums[l])
		cnt += r - mid - 1
	}
	for ; r <= right; r++ {
		tmp = append(tmp, nums[r])
	}
	// copy merge result
	for i := left; i <= right; i++ {
		nums[i] = tmp[i-left]
	}
	return cnt
}

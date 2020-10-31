package leetcode

import (
	"fmt"
	"go-algorithm/tree"
	"go-algorithm/util"
	"sort"
	"strings"
)

/*3. 无重复字符的最长子串

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

思路：双指针
*/
func LengthOfLongestSubstring(s string) int {
	str := []byte(s)
	cache := make(map[byte]struct{})
	// result
	res := 0
	// two pointers
	left := 0
	for right, ch := range str {
		if _, ok := cache[ch]; ok {
			// delete characters until meet duplicated character
			for ; left < right && str[left] != ch; left++ {
				delete(cache, str[left])
			}
			left++ // move left pointer forward
		} else {
			// add character in map
			cache[ch] = struct{}{}
			// get the max of length
			res = util.MaxInt(res, right-left+1)
		}
	}
	return res
}

/*
11. 盛最多水的容器
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

*/
func MaxArea(height []int) int {
	res := 0
	l, r := 0, len(height)-1
	hl, hr := 0, 0
	for l < r {
		hl, hr = height[l], height[r]
		res = util.MaxInt(res, (r-l)*util.MinInt(hl, hr))
		if hl < hr {
			l++
		} else {
			r--
		}
	}
	return res
}

/*
15. 三数之和

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。



示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

思路：
1 排序
2 三个指针，两层循环遍历

*/
func ThreeSum(nums []int) [][]int {
	res := [][]int{}
	length := len(nums)
	if length < 3 {
		return res
	}
	sort.Ints(nums)
	var l, r, sum int
	for i := 0; i < length-2; i++ {
		if i != 0 && nums[i] == nums[i-1] {
			continue
		}
		if nums[i] > 0 {
			break
		}
		for l, r = i+1, length-1; l < r; {
			sum = nums[i] + nums[l] + nums[r]
			if sum > 0 {
				r--
			} else if sum < 0 {
				l++
			} else {
				// 添加到结果中
				res = append(res, []int{nums[i], nums[l], nums[r]})
				l++
				r--
				for l < r && nums[l] == nums[l-1] {
					l++
				}
				for l < r && nums[r] == nums[r+1] {
					r--
				}
			}
		}
	}
	return res
}

/*
16. 最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

思路：和15题类似，可以不去重
*/
func ThreeSumClosest(nums []int, target int) int {
	sort.Ints(nums)
	closest := nums[0] + nums[1] + nums[2] //初值随意
	var l, r, sum int
	for i := 0; i < len(nums)-2; i++ {
		if i != 0 && nums[i] == nums[i-1] {
			continue
		}
		for l, r = i+1, len(nums)-1; l < r; {
			sum = nums[i] + nums[l] + nums[r]
			if util.AbsInt(sum-target) < util.AbsInt(closest-target) {
				closest = sum
			}
			if sum < target {
				l++
				for l < r && nums[l] == nums[l-1] {
					l++
				}
			} else if sum > target {
				r--
				for l < r && nums[r] == nums[r+1] {
					r--
				}
			} else {
				return target
			}
		}
	}
	return closest
}

// 26. 删除排序数组中的重复项,快慢双指针
func RemoveDuplicates(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	slow, fast := 1, 1
	for ; fast < len(nums); fast++ {
		if nums[fast] == nums[fast-1] {
			continue
		}
		nums[slow] = nums[fast]
		slow++
	}
	return slow
}

// 27. 移除元素,给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。快慢双指针
func RemoveElement(nums []int, val int) int {
	slow, fast := 0, 0
	for ; fast < len(nums); fast++ {
		if nums[fast] == val {
			continue
		}
		nums[slow] = nums[fast]
		slow++
	}
	return slow
}

/*
31. 下一个排列
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

1 4 3 2 -> 2 1 3 4
2 4 3 1 -> 3 1 2 4
*/
func NextPermutation(nums []int) {
	length := len(nums)
	if length < 2 {
		return
	}
	i := len(nums) - 1
	for ; i > 0; i-- {
		if nums[i-1] < nums[i] { // ascent pair
			break
		}
	}

	if i > 0 {
		pivot := nums[i-1]
		j := i
		for ; j < length-1; j++ {
			if nums[j+1] <= pivot {
				break
			}
		}
		nums[j], nums[i-1] = nums[i-1], nums[j] // swap nums[j] and nums[i-1]
	}
	reverse(nums[i:])
}

func reverse(nums []int) {
	l := len(nums)
	for i := 0; i < l/2; i++ {
		nums[i], nums[l-1-i] = nums[l-1-i], nums[i]
	}
}

// 48
func Rotate(matrix [][]int) {
	// transpose matrix

	for i := 0; i < len(matrix); i++ {
		for j := i + 1; j < len(matrix); j++ {
			fmt.Println(i, j)
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		}
	}
	fmt.Println(matrix)
	// reverse each row
	for i := 0; i < len(matrix); i++ {
		reverse(matrix[i])
	}

	fmt.Println(matrix)
}

type SortableString []rune

func (str SortableString) Len() int {
	return len(str)
}
func (str SortableString) Less(i, j int) bool {
	return str[i] < str[j]
}
func (str SortableString) Swap(i, j int) {
	str[i], str[j] = str[j], str[i]
}

func SortedString(str string) string {
	r := SortableString(str)
	sort.Sort(r)
	return string(r)
}

type counter [26]byte

/* 49. 字母异位词分组
散列计数法
*/
func GroupAnagrams(strs []string) [][]string {
	res := make(map[counter][]string)
	for _, str := range strs {
		cnt := counter{}
		for _, ch := range []byte(str) {
			cnt[ch-97]++
		}
		res[cnt] = append(res[cnt], str)
	}
	ret := [][]string{}
	for _, v := range res {
		ret = append(ret, v)
	}
	return ret
}

// 排序法
func GroupAnagramsMethod1(strs []string) [][]string {
	tmp := make(map[string][]string)
	for _, str := range strs {
		sorted := SortedString(str)
		v := tmp[sorted]
		v = append(v, str)
		tmp[sorted] = v
	}
	var res [][]string
	for _, v := range tmp {
		res = append(res, v)
	}
	return res
}

// 50.
func MyPow(x float64, n int) float64 {
	if n == 0 {
		return 1.0
	}
	if n == 1 {
		return x
	}
	if n < 0 {
		return 1.0 / MyPow(x, -n)
	}
	// x^n *x^n = x ^ 2n
	newN := n >> 1
	remain := n - 2*newN
	tmp := MyPow(x, newN)
	if remain == 0 {
		return tmp * tmp
	}
	return tmp * tmp * x
}

// 51. N皇后
func SolveNQueens(n int) [][]string {
	checkboard := makeCheckborad(n)
	queens := make([]position, 0)
	tmp := make([][]position, 0)
	nQueens(checkboard, n, &queens, 0, &tmp)
	res := [][]string{}
	for _, sol := range tmp {
		x := make([]string, 0)
		for _, pos := range sol {
			x = append(x, makeString(n, pos.y))
		}
		res = append(res, x)

	}
	return res
}
func makeString(size, i int) string {
	s := make([]rune, size)
	for x := 0; x < size; x++ {
		if x == i {
			s[x] = 'Q'
		} else {
			s[x] = '.'
		}
	}
	return string(s)
}

type position struct {
	x, y int
}

func nQueens(board [][]int, n int, queens *[]position, row int, res *[][]position) {
	if n == 0 {
		dst := make([]position, len(*queens))
		copy(dst, *queens)
		*res = append(*res, dst)
	}
	// 只能放在row和row以下的行，防止重复
	for i := row; i < len(board); i++ {
		for j := 0; j < len(board); j++ {
			// not attacked
			if board[i][j] == 0 {
				pos := position{i, j}
				// fmt.Println("add queen", pos)
				addQueen(board, pos)
				// fmt.Println(n - 1)
				// printCheckborad(board)
				*queens = append(*queens, pos)
				nQueens(board, n-1, queens, i+1, res)
				// fmt.Println("del queen", pos)
				removeQueen(board, pos)
				*queens = (*queens)[:len(*queens)-1]
			}
		}
	}
}
func printCheckborad(board [][]int) {
	fmt.Println("--------------")
	for i := 0; i < len(board); i++ {
		fmt.Println(board[i])
	}
	fmt.Println("--------------")
}

func addQueen(board [][]int, pos position) {
	for i := 0; i < len(board); i++ {
		board[i][pos.y] += 1
	}
	for i := 0; i < len(board); i++ {
		board[pos.x][i] += 1
	}
	for i, j := pos.x-1, pos.y-1; i > -1 && j > -1; i, j = i-1, j-1 {
		board[i][j] += 1
	}
	for i, j := pos.x+1, pos.y+1; i < len(board) && j < len(board); i, j = i+1, j+1 {
		board[i][j] += 1
	}
	for i, j := pos.x+1, pos.y-1; i < len(board) && j > -1; i, j = i+1, j-1 {
		board[i][j] += 1
	}
	for i, j := pos.x-1, pos.y+1; i > -1 && j < len(board); i, j = i-1, j+1 {
		board[i][j] += 1
	}
	board[pos.x][pos.y] -= 1
}
func removeQueen(board [][]int, pos position) {
	for i := 0; i < len(board); i++ {
		board[i][pos.y] -= 1
	}
	for i := 0; i < len(board); i++ {
		board[pos.x][i] -= 1
	}
	for i, j := pos.x-1, pos.y-1; i > -1 && j > -1; i, j = i-1, j-1 {
		board[i][j] -= 1
	}
	for i, j := pos.x+1, pos.y+1; i < len(board) && j < len(board); i, j = i+1, j+1 {
		board[i][j] -= 1
	}
	for i, j := pos.x+1, pos.y-1; i < len(board) && j > -1; i, j = i+1, j-1 {
		board[i][j] -= 1
	}
	for i, j := pos.x-1, pos.y+1; i > -1 && j < len(board); i, j = i-1, j+1 {
		board[i][j] -= 1
	}
	board[pos.x][pos.y] += 1
}
func makeCheckborad(n int) [][]int {
	check := make([][]int, n)
	for i := 0; i < n; i++ {
		check[i] = make([]int, n)
	}
	return check
}

// 55
func CanJump(nums []int) bool {
	// 贪心算法
	// 从头开始遍历数组，每次计算最大可以走到的位置maxIdx
	// 如果maxIdx >= 数组末尾，返回true
	// 否则返回false
	// 一开始想的是从后往前递归，但是复杂度太高了，提交是超时的
	lng := len(nums)
	if lng == 0 {
		return false
	}
	if lng == 1 {
		return true
	}
	lastIdx := lng - 1
	maxIdx := 0
	for i := 0; i <= maxIdx; i++ {
		tmp := i + nums[i]
		if tmp > maxIdx {
			maxIdx = tmp
		}
		if maxIdx >= lastIdx {
			return true
		}
	}
	return false
}

// 54 spiral matrix
func SpiralOrder(matrix [][]int) []int {
	if len(matrix) == 0 {
		return make([]int, 0)
	}
	row, col := len(matrix), len(matrix[0])
	// 生成row*col bool矩阵
	seen := newBoolMatrix(row, col)
	// direction trick!
	dx := []int{0, 1, 0, -1}
	dy := []int{1, 0, -1, 0}
	di, x, y, newX, newY := 0, 0, 0, 0, 0
	res := make([]int, row*col) // 返回值长度是固定的
	for i := 0; i < row*col; i++ {
		res[i] = matrix[x][y]
		seen[x][y] = true
		newX = x + dx[di]
		newY = y + dy[di]
		if newX < 0 || newY < 0 || newX == row || newY == col || seen[newX][newY] {
			// clock-wise
			di = (di + 1) % 4
			newX = x + dx[di]
			newY = y + dy[di]
		}
		x, y = newX, newY
	}
	return res
}

func newBoolMatrix(x, y int) [][]bool {
	mtx := make([][]bool, x)
	for i := 0; i < x; i++ {
		mtx[i] = make([]bool, y)
	}
	return mtx
}

type sortableIntervals [][]int

func (interval sortableIntervals) Len() int {
	return len(interval)
}
func (interval sortableIntervals) Swap(i, j int) {
	interval[i], interval[j] = interval[j], interval[i]
}
func (interval sortableIntervals) Less(i, j int) bool {
	return interval[i][0] < interval[j][0]
}

// 56 合并区间
func Merge(intervals [][]int) [][]int {
	// 贪心算法，需要数学证明，看Leetcode
	if len(intervals) <= 1 {
		return intervals
	}
	sort.Sort(sortableIntervals(intervals))
	res := [][]int{intervals[0]}
	for i := 1; i < len(intervals); i++ {
		cur := intervals[i]
		last := res[len(res)-1]
		fmt.Println(last, cur)
		if last[1] >= cur[0] {
			if cur[1] > last[1] {
				last[1] = cur[1]
			}

		} else {
			res = append(res, cur)
		}
	}
	return res
}

/*
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/
// 59 生成螺旋矩阵
func GenerateMatrix(n int) [][]int {
	return nil
}

func GenerateMatrixMethod1(n int) [][]int {
	mtx := make([][]int, n)
	seen := make([][]bool, n)
	for i := 0; i < n; i++ {
		mtx[i] = make([]int, n)
		seen[i] = make([]bool, n)
	}
	dx := []int{0, 1, 0, -1}
	dy := []int{1, 0, -1, 0}
	di, x, y, newX, newY := 0, 0, 0, 0, 0
	for i := 1; i <= n*n; i++ {
		mtx[x][y] = i
		seen[x][y] = true
		newX, newY = x+dx[di], y+dy[di]
		if newX < 0 || newY < 0 || newX == n || newY == n || seen[newX][newY] {
			di = (di + 1) % 4
			newX, newY = x+dx[di], y+dy[di]
		}
		x, y = newX, newY
	}
	return mtx
}

//63. 不同路径 II
/*
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

思路：动态规划状态方程
*/
func UniquePathsWithObstacles(obstacleGrid [][]int) int {
	if len(obstacleGrid) == 0 {
		return 0
	}
	if obstacleGrid[0][0] == 1 {
		return 0
	}
	obstacleGrid[0][0] = 1
	r, c := len(obstacleGrid), len(obstacleGrid[0])
	for i := 1; i < r; i++ {
		if obstacleGrid[i][0] == 1 {
			for ii := i; ii < r; ii++ {
				obstacleGrid[ii][0] = 0
			}
			break
		}
		obstacleGrid[i][0] = 1
	}
	for i := 1; i < c; i++ {
		if obstacleGrid[0][i] == 1 {
			for ii := i; ii < c; ii++ {
				obstacleGrid[0][ii] = 0
			}
			break
		}
		obstacleGrid[0][i] = 1
	}
	for i := 1; i < r; i++ {
		for j := 1; j < c; j++ {
			if obstacleGrid[i][j] == 1 {
				obstacleGrid[i][j] = 0
			} else {
				obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
			}
		}
	}
	return obstacleGrid[r-1][c-1]
}

/*
64. 最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
*/
func MinPathSum(grid [][]int) int {
	if len(grid) == 0 {
		return 0
	}
	r, c := len(grid), len(grid[0])
	for i := 1; i < r; i++ {
		grid[i][0] += grid[i-1][0]
	}
	for i := 1; i < c; i++ {
		grid[0][i] += grid[0][i-1]
	}
	for i := 1; i < r; i++ {
		for j := 1; j < c; j++ {
			grid[i][j] += util.MinInt(grid[i-1][j], grid[i][j-1])
		}
	}
	return grid[r-1][c-1]
}

/*
71. 简化路径
以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。
在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。更多信息请参阅：Linux / Unix中的绝对路径 vs 相对路径
请注意，返回的规范路径必须始终以斜杠 / 开头，并且两个目录名之间必须只有一个斜杠 /。最后一个目录名（如果存在）不能以 / 结尾。此外，规范路径必须是表示绝对路径的最短字符串。

示例 1：

输入："/home/"
输出："/home"
解释：注意，最后一个目录名后面没有斜杠。
示例 2：

输入："/../"
输出："/"
解释：从根目录向上一级是不可行的，因为根是你可以到达的最高级。
示例 3：

输入："/home//foo/"
输出："/home/foo"
解释：在规范路径中，多个连续斜杠需要用一个斜杠替换。
示例 4：

输入："/a/./b/../../c/"
输出："/c"
示例 5：

输入："/a/../../b/../c//.//"
输出："/c"
示例 6：

输入："/a//b////c/d//././/.."
输出："/a/b/c"

思路：栈
*/
func SimplifyPath(path string) string {
	strs := strings.Split(path, "/")
	stack := make([]string, 0)
	for _, str := range strs {
		if str == "." || str == "" {
			continue
		}
		if str == ".." {
			if len(stack) > 0 {
				stack = stack[:len(stack)-1]
			}
			continue
		}
		stack = append(stack, str)
	}
	return "/" + strings.Join(stack, "/")
}

/*
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:

输入:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

思路：记录0的行数和列数

官方解答有O(1)的空间复杂度
在给定数字范围的情况下，把要标记成0的值暂时赋为范围外的某个值，表示虚值
在第二次遍历的时候把虚值都赋为0
*/
func SetMatrix(matrix [][]int) {
	if len(matrix) == 0 {
		return
	}
	if len(matrix) == 1 && len(matrix[0]) == 0 {
		return
	}
	r, c := len(matrix), len(matrix[0])
	rowSet, colSet := make(map[int]struct{}), make(map[int]struct{})
	for i := 0; i < r; i++ {
		for j := 0; j < c; j++ {
			if matrix[i][j] == 0 {
				rowSet[i] = struct{}{}
				colSet[j] = struct{}{}
			}
		}
	}
	for i := 0; i < r; i++ {
		for j := 0; j < c; j++ {
			if _, find := rowSet[i]; find {
				matrix[i][j] = 0
				continue
			}
			if _, find := colSet[j]; find {
				matrix[i][j] = 0
			}
		}
	}
}

/*
74. 搜索二维矩阵

编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

    每行中的整数从左到右按升序排列。
    每行的第一个整数大于前一行的最后一个整数。

示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
*/
func SearchMatrix(matrix [][]int, target int) bool {
	if len(matrix) == 0 {
		return false
	}
	// start search from top right corner
	for i, j := 0, len(matrix[0])-1; i < len(matrix) && j > -1; {
		cur := matrix[i][j]
		if cur == target {
			return true
		}
		if cur > target {
			j--
			continue
		}
		i++
	}
	return false
}

/*
75. 颜色分类

给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]

进阶：

    一个直观的解决方案是使用计数排序的两趟扫描算法。
    首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
    你能想出一个仅使用常数空间的一趟扫描算法吗？
*/
func SortColors(nums []int) {
	left, cur, right := 0, 0, len(nums)-1
	for cur <= right {
		tmp := nums[cur]
		if tmp == 0 {
			nums[left], nums[cur] = nums[cur], nums[left]
			left++
			cur++
		} else if tmp == 1 {
			cur++
		} else {
			nums[right], nums[cur] = nums[cur], nums[right]
			right--
		}
	}
}

/*
78. 子集

给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

backtrack, iterate over the length of subsets
*/
func Subsets(nums []int) [][]int {
	res := [][]int{}
	for lenSubset := 0; lenSubset <= len(nums); lenSubset++ {
		res = append(res, backtrackSubsets(nums, lenSubset, 0, []int{})...)
	}
	return res
}

func backtrackSubsets(nums []int, lenSubset, start int, curr []int) [][]int {
	if len(curr) == lenSubset {
		// cut the branch
		tmp := make([]int, len(curr))
		copy(tmp, curr)
		return [][]int{tmp}
	}
	res := [][]int{}
	for i := start; i < len(nums); i++ {
		curr = append(curr, nums[i])
		res = append(res, backtrackSubsets(nums, lenSubset, i+1, curr)...)
		curr = curr[:len(curr)-1]
	}
	return res
}

/*
79. 单词搜索

给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。


示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false

2D backtrack
*/
func Exist(board [][]byte, word string) bool {
	r, c := len(board), len(board[0])
	wordByte := []byte(word)
	visited := newVisitedMatrix(r, c)
	for i := 0; i < r; i++ {
		for j := 0; j < c; j++ {
			ok := backtrackExist(i, j, wordByte, board, visited)
			if ok {
				return true
			}
		}
	}
	return false
}

func backtrackExist(x, y int, word []byte, board [][]byte, visited [][]bool) bool {
	if len(word) == 0 {
		return true
	}
	if x == -1 ||
		y == -1 ||
		x == len(board) ||
		y == len(board[0]) ||
		board[x][y] != word[0] ||
		visited[x][y] {
		return false
	}
	visited[x][y] = true
	res := backtrackExist(x, y-1, word[1:], board, visited) ||
		backtrackExist(x-1, y, word[1:], board, visited) ||
		backtrackExist(x, y+1, word[1:], board, visited) ||
		backtrackExist(x+1, y, word[1:], board, visited)
	visited[x][y] = false
	return res
}

func newVisitedMatrix(r, c int) [][]bool {
	vst := make([][]bool, r)
	for i := 0; i < r; i++ {
		vst[i] = make([]bool, c)
	}
	return vst
}

/*
80. 删除排序数组中的重复项 II

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定 nums = [1,1,1,2,2,3],

函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。

你不需要考虑数组中超出新长度后面的元素。

示例 2:

给定 nums = [0,0,1,1,1,1,2,3,3],

函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。

你不需要考虑数组中超出新长度后面的元素。

说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

double pointer
*/
func RemoveDuplicates2(nums []int) int {
	lng := len(nums)
	if lng < 3 {
		return lng
	}
	idxSlow := 1
	cnt := 1
	for idxFast := 1; idxFast < lng; idxFast++ {
		if nums[idxFast] != nums[idxFast-1] {
			nums[idxSlow] = nums[idxFast]
			idxSlow++
			cnt = 1
			continue
		}
		if cnt < 2 {
			nums[idxSlow] = nums[idxFast]
			idxSlow++
		}
		cnt++
	}
	return idxSlow
}

/*
86. 分隔链表
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5

双指针
*/
func Partition(head *ListNode, x int) *ListNode {
	before, after := &ListNode{0, nil}, &ListNode{0, nil}
	beforeHead, afterHead := before, after
	for head != nil {
		if head.Val < x {
			before.Next = head
			before = before.Next
		} else {
			after.Next = head
			after = after.Next
		}
		head = head.Next
	}
	after.Next = nil
	before.Next = afterHead.Next
	return beforeHead.Next
}

/*
89. 格雷码，比较难想
n=0: [0]
n=1: [0 1]
n=2: [00 01 10 11] 前一位是0 1,后一位是根据数组的中点对称的
n=3: [000 001 010 011 111 110 101 100] 前一位是0 1,后两位根据数组的中点对称的
...
*/
func GrayCode(n int) []int {
	nn := uint(n)
	res := []int{0}
	for i := uint(0); i < nn; i++ {
		add := 1 << i
		for j := len(res) - 1; j > -1; j-- {
			res = append(res, add+res[j])
		}
	}
	return res
}

type ListNode struct {
	Val  int
	Next *ListNode
}

/*
94. 二叉树中序遍历
有3种方法，递归，栈，Morris线索二叉树
inorder traversal
*/
func InorderTraversal(root *tree.TreeNode) []int {
	res := make([]int, 0)
	stack := make([]*tree.TreeNode, 0)
	cur := root
	for cur != nil || len(stack) > 0 {
		for cur != nil {
			stack = append(stack, cur)
			cur = cur.Left
		}
		top := stack[len(stack)-1]
		res = append(res, top.Val)
		stack = stack[:len(stack)-1]
		cur = top.Right
	}
	return res
}

// Morris 算法 114也用到了类似的方法
func InorderTraversalMorris(root *tree.TreeNode) []int {
	res := make([]int, 0)
	cur := root
	for cur != nil {
		if cur.Left == nil {
			res = append(res, cur.Val)
			cur = cur.Right
		} else {
			tmp := cur.Left
			for tmp.Right != nil {
				tmp = tmp.Right
			}
			tmp.Right = cur
			cur = cur.Left
			tmp.Right.Left = nil // 删除左子树引用 important
		}
	}
	return res
}

func InorderTraversalRecursive(root *tree.TreeNode) []int {
	res := make([]int, 0)
	traversalRecursive(root, &res)
	return res
}

func traversalRecursive(root *tree.TreeNode, res *[]int) {
	if root == nil {
		return
	}
	traversalRecursive(root.Left, res)
	*res = append(*res, root.Val)
	traversalRecursive(root.Right, res)
}

// TODO 前序 后序遍历

/*
95. 不同的二叉搜索树II
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
*/
func GenerateTrees(n int) []*tree.TreeNode {
	if n == 0 {
		return nil
	}
	return generateTreesRecursive(1, n)
}

func generateTreesRecursive(start, end int) []*tree.TreeNode {
	if start > end {
		return []*tree.TreeNode{nil}
	}
	res := make([]*tree.TreeNode, 0)
	for i := start; i <= end; i++ {
		leftTrees := generateTreesRecursive(start, i-1)
		rightTrees := generateTreesRecursive(i+1, end)
		for _, leftTree := range leftTrees {
			for _, rightTree := range rightTrees {
				currentTree := &tree.TreeNode{Val: i}
				currentTree.Left = leftTree
				currentTree.Right = rightTree
				res = append(res, currentTree)
			}
		}
	}
	return res
}

/*
96. 不同的二叉搜索树

给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

思路：二叉树，动态规划
*/
func NumTrees(n int) int {
	dp := make([]int, n+1)
	dp[0] = 1
	dp[1] = 1
	for i := 2; i <= n; i++ {
		for j := 0; j < n; j++ {
			dp[j] += dp[j] + dp[i-j-1]
		}
	}
	return dp[n]
}

// 递归解，太慢
func NumTreesRecursive(n int) int {
	if n == 0 || n == 1 {
		return n
	}
	sum := 0
	for i := 0; i < n; i++ {
		sum += NumTreesRecursive(i) * NumTreesRecursive(n-i-1)
	}
	return sum
}

/*
98. 验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

    节点的左子树只包含小于当前节点的数。
    节点的右子树只包含大于当前节点的数。
    所有左子树和右子树自身必须也是二叉搜索树。

示例 1:

输入:
    2
   / \
  1   3
输出: true

示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
思路：有2种办法，递归和中序遍历
*/
const INT_MAX = int(^uint(0) >> 1)
const INT_MIN = ^INT_MAX

func IsValidBST(root *tree.TreeNode) bool {
	return isValidBSTRange(root, INT_MIN, INT_MAX)
}
func isValidBSTRange(root *tree.TreeNode, min, max int) bool {
	if root == nil {
		return true
	}
	if root.Val > min && root.Val < max && isValidBSTRange(root.Left, min, root.Val) && isValidBSTRange(root.Right, root.Val, max) {
		return true
	}
	return false
}

// inorder traversal
func IsValidBSTTraversal(root *tree.TreeNode) bool {
	traversal := make([]int, 0)
	isValidBSTTraversal(root, &traversal)
	if len(traversal) < 2 {
		return true
	}
	for i := 1; i < len(traversal); i++ {
		if traversal[i] <= traversal[i-1] {
			return false
		}
	}
	return true
}

func isValidBSTTraversal(root *tree.TreeNode, res *[]int) {
	if root == nil {
		return
	}
	isValidBSTTraversal(root.Left, res)
	*res = append(*res, root.Val)
	isValidBSTTraversal(root.Right, res)
}

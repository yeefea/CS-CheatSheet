// +build ignore

package main

import "fmt"

/*
棋盘覆盖问题
递归
*/

func main() {
	board := FillChessboard(8, 2, 2)
	printChessboard(board)
}

// FillChessboard size 棋盘大小, 必须为2^k, x,y奇点所在
func FillChessboard(size, x, y int) [][]int {
	if !IsPowerOfTwo(size) {
		return nil
	}
	chessboard := make([][]int, size)
	for i := 0; i < size; i++ {
		chessboard[i] = make([]int, size)
	}
	chessboard[x][y] = -1
	cnt := 1
	fill(size, 0, 0, x, y, &cnt, chessboard)
	chessboard[x][y] = 0
	return chessboard
}

func fill(size, left, top, x, y int, cnt *int, chessboard [][]int) {
	if size == 1 {
		return
	}
	size /= 2
	midX, midY := left+size, top+size
	oriCnt := *cnt
	*cnt++
	var tmpX, tmpY int
	// I
	if x < midX && y < midY {
		fill(size, left, top, x, y, cnt, chessboard)
	} else {
		tmpX, tmpY = midX-1, midY-1
		chessboard[tmpX][tmpY] = oriCnt
		fill(size, left, top, midX-1, midY-1, cnt, chessboard)
	}
	// II
	if x >= midX && y < midY {
		fill(size, midX, top, x, y, cnt, chessboard)
	} else {
		tmpX, tmpY = midX, midY-1
		chessboard[tmpX][tmpY] = oriCnt
		fill(size, midX, top, midX, midY-1, cnt, chessboard)
	}
	// III
	if x < midX && y >= midY {
		fill(size, left, midY, x, y, cnt, chessboard)
	} else {
		tmpX, tmpY = midX-1, midY
		chessboard[tmpX][tmpY] = oriCnt
		fill(size, left, midY, midX-1, midY, cnt, chessboard)
	}
	// IV
	if x >= midX && y >= midY {
		fill(size, midX, midY, x, y, cnt, chessboard)
	} else {
		tmpX, tmpY = midX, midY
		chessboard[tmpX][tmpY] = oriCnt
		fill(size, midX, midY, midX, midY, cnt, chessboard)
	}
}

// IsPowerOfTwo 判断一个数是否是2的整数次幂
func IsPowerOfTwo(n int) bool {
	// 如果一个数是2的整数次幂，则其二进制形式有一个特点
	// 除了最高位为1，其余位全为0
	// 此时可以借鉴求取二进制中1的个数的方法
	return 0 == (n & (n - 1))
}

func printChessboard(chessboard [][]int) {
	for i := 0; i < len(chessboard); i++ {
		for j := 0; j < len(chessboard); j++ {
			fmt.Printf("%d\t", chessboard[i][j])
		}
		fmt.Println()
	}
}

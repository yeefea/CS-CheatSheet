package leetcode

/*
1143. 最长公共子序列
*/
func LongestCommonSubsequence(text1 string, text2 string) int {
	dp := make([][]int, len(text1))
	bytes1 := []byte(text1)
	bytes2 := []byte(text2)
	for i := 0; i < len(bytes1); i++ {
		dp[i] = make([]int, len(bytes2))
		for j := 0; j < len(bytes2); j++ {
			if bytes1[i] == bytes2[j] {
				dp[i][j] = dpWrapper(dp, i-1, j-1) + 1
			} else {
				m := dpWrapper(dp, i-1, j)
				n := dpWrapper(dp, i, j-1)
				if m > n {
					dp[i][j] = m
				} else {
					dp[i][j] = n
				}
			}
		}
	}
	return dp[len(text1)-1][len(text2)-1]
}

func dpWrapper(dp [][]int, i, j int) int {
	if i < 0 || j < 0 {
		return 0
	}
	return dp[i][j]
}

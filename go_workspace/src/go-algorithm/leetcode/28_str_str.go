// +build ignore

package main

import "fmt"

func main() {
	fmt.Println(strStr("hello", "ll"))
	fmt.Println(strStr("a", "a"))
	fmt.Println(strStr("hello", ""))
	fmt.Println(strStr("", "ll"))
}

func strStr(haystack string, needle string) int {
	if len(needle) == 0 {
		return 0
	}
	if len(needle) > len(haystack) {
		return -1
	}
	// 这里要等号 比如len(haystack)==1 && len(needle)==1时需要一次循环
	for i := 0; i <= len(haystack)-len(needle); i++ {
		found := true
		// 向后依次比较每一位字符
		for j := 0; j < len(needle); j++ {
			if haystack[i+j] != needle[j] {
				// 发现不同的字符，匹配失败跳出循环
				found = false
				break
			}
		}
		// 完全相同，返回起始坐标
		if found {
			return i
		}
	}
	return -1
}

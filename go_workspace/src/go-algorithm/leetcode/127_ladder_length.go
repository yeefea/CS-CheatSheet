// +build ignore

package main

import "fmt"

/*
127. 单词接龙

给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

    每次转换只能改变一个字母。
    转换过程中的中间单词必须是字典中的单词。

说明:

    如果不存在这样的转换序列，返回 0。
    所有单词具有相同的长度。
    所有单词只由小写字母组成。
    字典中不存在重复的单词。
    你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。

示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: 0

解释: endWord "cog" 不在字典中，所以无法进行转换。

思路: 图的广度优先搜索
*/

type Pair struct {
	S     string
	Level int
}

func ladderLength(beginWord string, endWord string, wordList []string) int {
	wordLen := len(beginWord)
	if wordLen == 0 {
		return 0
	}
	comboMap := make(map[string]*[]string)
	for _, x := range wordList {
		for i := 0; i < wordLen; i++ {
			combo := x[:i] + "*" + x[i+1:]
			sli, ok := comboMap[combo]
			if ok {
				*sli = append(*sli, x)
			} else {
				sli = &[]string{x}
				comboMap[combo] = sli
			}
		}
	}
	visited := make(map[string]struct{})
	queue := []Pair{Pair{beginWord, 1}}
	for len(queue) > 0 {
		pair := queue[0]
		x, lvl := pair.S, pair.Level
		for i := 0; i < wordLen; i++ {
			combo := x[:i] + "*" + x[i+1:]
			adj := comboMap[combo]
			if adj != nil {
				for _, word := range *adj {
					if word == endWord {
						return lvl + 1
					}
					if _, ok := visited[word]; !ok {
						queue = append(queue, Pair{word, lvl + 1})
						visited[word] = struct{}{}
					}
				}
			}
		}
		queue = queue[1:]
	}
	return 0
}

func main() {
	beginWord, endWord := "hit", "cog"
	wordList := []string{"hot", "dot", "dog", "lot", "log", "cog"}
	res := ladderLength(beginWord, endWord, wordList)
	fmt.Println(res)
}

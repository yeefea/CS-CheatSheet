package main

import "fmt"

func main() {
	a := byte('a')
	fmt.Println(a)
	dict := make(map[[26]byte]int)
	fmt.Println(dict)
}

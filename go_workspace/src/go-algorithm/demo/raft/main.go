package main

import (
	"fmt"
	"time"
)

func main() {
	tk := time.NewTicker(1 * time.Second)
	for i := 0; i < 3; i++ {
		_ = <-tk.C
		fmt.Println(i)
	}
	tk.Stop()
	time.Sleep(1 * time.Second)
}

package util

import (
	"fmt"
	"testing"
)

func TestIsPrime(t *testing.T) {
	for i := 100000; i > 2; i-- {
		if IsPrime(i) {
			fmt.Println(i)
			break
		}
	}
}

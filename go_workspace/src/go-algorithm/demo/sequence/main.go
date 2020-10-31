package main

import (
	"fmt"
	"go-algorithm/sequence"
)

func main() {

	gens := []sequence.SequenceGenerator{
		sequence.NewFibonacciSequence,
		sequence.NewLucasSequence,
		sequence.NewPellSequence,
		sequence.NewCatalanSequence,
		sequence.NewTriangularSequence,
		sequence.NewPentagonalSequence,
	}
	for _, fnc := range gens {
		for i := 0; i < 10; i++ {
			fmt.Println(fnc(i))
		}
	}
}

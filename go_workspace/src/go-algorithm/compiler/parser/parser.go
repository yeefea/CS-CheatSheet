package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode"
)

var (
	reader = bufio.NewReader(os.Stdin)
)

type parser struct {
	lookahead byte
}

func NewParser() parser {
	la, err := reader.ReadByte()
	if err != nil {
		panic("error")
	}
	return parser{la}
}

func (parser *parser) expr() {
	parser.term()
	for {
		if parser.lookahead == '+' {
			parser.match('+')
			parser.term()
			fmt.Printf("+")
		} else if parser.lookahead == '-' {
			parser.match('-')
			parser.term()
			fmt.Printf("-")
		} else {
			return
		}
	}
}

func (parser *parser) term() {
	if unicode.IsDigit(rune(parser.lookahead)) {
		fmt.Printf("%c", parser.lookahead)
		parser.match(parser.lookahead)
	} else {
		panic("syntax error")
	}
}

func (parser *parser) match(ch byte) {
	var err error
	if parser.lookahead == ch {
		parser.lookahead, err = reader.ReadByte()
		// fmt.Println("new la", parser.lookahead)
		if err != nil {
			panic("syntax error")
		}
	} else {
		panic("syntax error")
	}
}

func main() {
	parser := NewParser()
	parser.expr()
}

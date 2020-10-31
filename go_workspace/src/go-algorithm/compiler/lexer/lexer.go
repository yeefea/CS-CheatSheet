package main

import "fmt"

type lexer struct {
	lineNo    int
	source    []rune
	lenSource int
	idx       int
}

func NewLexer(source string) lexer {
	src := []rune(source)
	return lexer{lineNo: 1, source: src, lenSource: len(src)}
}

func (lexer *lexer) peek() rune {
	return lexer.source[lexer.idx]
}

func (lexer *lexer) hasNextChar() bool {
	return lexer.idx < len(lexer.source)
}

func (lexer *lexer) nextChar() rune {
	ret := lexer.source[lexer.idx]
	lexer.idx++
	return ret
}

func (lexer *lexer) scan() {
	for lexer.hasNextChar() {
		ch := lexer.nextChar()
		if ch == ' ' || ch == '\t' {
			continue
		}
		if ch == '\n' {
			lexer.lineNo++
			continue
		}
		fmt.Printf("%c", ch)
	}
}

func main() {
	lex := NewLexer("1+2 1231231=113")
	lex.scan()
}

package stack

/*
push series: 12345
pop series: 32541

stack:
push(123)	top	->	3	2	1
pop(3)		top	->		2	1
pop(2)		top	->			1
push(45)	top	->	5	4	1
pop(5)		top	->		4	1
pop(4)		top	->			1
pop(1)		top	-> 	nil
*/

// IsPopSerial pop serial
func IsPopSerial(pushList, popList []int) bool {
	/*
		pushList popList长度必须相等
		1. pushList入栈
		2. while 栈顶元素==popList首元素: 出栈,pop index++
		3. 最后栈为空 且 pop index == popList长度 => true,否则 => false
	*/
	pushLen := len(pushList)
	popLen := len(popList)
	if pushLen != popLen {
		return false
	}
	if pushLen == 0 {
		return true
	}
	stack := NewLinkedStack()
	popIdx := 0
	for _, push := range pushList {
		stack.Push(push)
		for !stack.IsEmpty() && popIdx < popLen && stack.Top() == popList[popIdx] {
			stack.Pop()
			popIdx++
		}
	}
	if stack.IsEmpty() && popIdx == popLen {
		return true
	}
	return false
}

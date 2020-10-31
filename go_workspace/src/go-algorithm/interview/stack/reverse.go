package stack

// ReverseStackRecursive reverse stack recursively, O(N^2) time complexity, O(1) space complexity
func ReverseStackRecursive(stack Stack) {
	if stack.IsEmpty() {
		return
	}
	bottom := popBottom(stack)
	ReverseStackRecursive(stack)
	stack.Push(bottom)
}

func popBottom(stack Stack) int {
	if stack.GetSize() == 1 {
		return stack.Pop()
	}
	top := stack.Pop()
	bottom := popBottom(stack)
	stack.Push(top)
	return bottom
}

package stack

// SortStack reverse stack recursively, O(N^2) time complexity, O(1) space complexity
// 类似于冒泡排序
func SortStack(stack Stack) {
	if stack.IsEmpty() {
		return
	}
	bottom := getSmallest(stack)
	SortStack(stack)
	stack.Push(bottom)
}

func getSmallest(stack Stack) int {
	if stack.GetSize() == 1 {
		return stack.Pop()
	}
	top := stack.Pop()
	small := getSmallest(stack)
	if top < small {
		stack.Push(small)
		return top
	}
	stack.Push(top)
	return small
}

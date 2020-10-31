package disjset

type disjSet []int

func NewDisjSet(size int) disjSet {
	set := make(disjSet, size)
	for i := 0; i < size; i++ {
		set[i] = -1
	}
	return set
}

// SetUnion 按高度求并
func (set disjSet) SetUnion(root1, root2 int) {
	root1 = set.Find(root1)
	root2 = set.Find(root2)
	if set[root2] < set[root1] {
		set[root1] = root2
	} else {
		if set[root1] == set[root2] {
			set[root1]--
		}
		set[root2] = root1
	}
}

func (set disjSet) Find(x int) int {
	if set[x] <= 0 {
		return x
	}
	set[x] = set.Find(set[x])
	return set[x]
}

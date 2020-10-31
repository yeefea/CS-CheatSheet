package sequence

/*
fibonacci a0=0 a1=1 a2=1, a[n]=a[n-1]+a[n-2]
lucas 1,3,4,7,11,18,29,47 a1=1 a2=3 an=an-1+an-2
pell a1=1, a2=2, a[n]=2a[n-1]+a[n-2]
triangular 1,3,6,10,15,... 3-1=2,6-3=3,10-6=4,15-10=5,21-15=6,...
square 1,4,9,16,25,... n*2
pentagonal 1,5,12,22,35,n(3n-1)/2
catalan 1 1 2 5 14 42 132 429 1430 4862 ...
		c[n] = c[n-1]*(4n-2)/(n+1), c[n] = C(2n,n)/(n+1)
		c[n] = C(2n,n)-c(2n,n-1)
stirling
两类stirling数
第一类
	s(n,m)将n个不同元素构成m个圆排列的数目
		无符号第一类s_u(n,m)
		有符号第一类s_s(n,m)
第二类
	S(n,m) 将n个不同的元素分成m个集合的方案数

*/
type SequenceGenerator func(int) []int

func NewFibonacciSequence(n int) []int {
	seq := make([]int, n)
	if n == 0 {
		return seq
	}
	seq[0] = 0
	if n == 1 {
		return seq
	}
	seq[1] = 1
	if n == 2 {
		return seq
	}
	for i := 2; i < n; i++ {
		seq[i] = seq[i-1] + seq[i-2]
	}
	return seq
}

func NewLucasSequence(n int) []int {
	seq := make([]int, n)
	if n == 0 {
		return seq
	}
	seq[0] = 1
	if n == 1 {
		return seq
	}
	seq[1] = 3
	if n == 2 {
		return seq
	}
	for i := 2; i < n; i++ {
		seq[i] = seq[i-1] + seq[i-2]
	}
	return seq
}

func NewPellSequence(n int) []int {
	seq := make([]int, n)
	if n == 0 {
		return seq
	}
	seq[0] = 0
	if n == 1 {
		return seq
	}
	seq[1] = 1
	if n == 2 {
		return seq
	}
	for i := 2; i < n; i++ {
		seq[i] = 2*seq[i-1] + seq[i-2]
	}
	return seq
}

func NewTriangularSequence(n int) []int {
	seq := make([]int, n)
	if n == 0 {
		return seq
	}
	seq[0] = 1
	if n == 1 {
		return seq
	}
	for i := 1; i < n; i++ {
		seq[i] = seq[i-1] + i + 1
	}
	return seq
}

func NewPentagonalSequence(n int) []int {
	seq := make([]int, n)
	for i := 1; i <= n; i++ {
		seq[i-1] = i * (3*i - 1) / 2
	}
	return seq

}

func NewCatalanSequence(n int) []int {
	seq := make([]int, n)
	if n == 0 {
		return seq
	}
	seq[0] = 1
	if n == 1 {
		return seq
	}
	seq[1] = 1
	if n == 2 {
		return seq
	}
	for i := 2; i < n; i++ {
		for j := 0; j < i; j++ {
			seq[i] += seq[j] * seq[i-j-1]
		}
	}
	return seq
}

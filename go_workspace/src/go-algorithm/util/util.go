package util

func AbsInt(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func MinInt(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func MaxInt(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func IsPrime(x int) bool {
	if x < 2 {
		return false
	}
	if x == 2 {
		return true
	}
	if x%2 == 0 {
		return false
	}
	// for i := 3; i < x; i++ {
	for i := 3; i*i <= x; i++ {
		if x%i == 0 {
			return false
		}
	}
	return true
}

func CompareBytes(b1, b2 []byte) bool {
	if len(b1) != len(b2) {
		return false
	}
	for i := 0; i < len(b1); i++ {
		if b1[i] != b2[i] {
			return false
		}
	}
	return true
}

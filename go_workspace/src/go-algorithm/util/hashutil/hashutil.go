package hashutil

import (
	"hash/fnv"
)

// HashFunc generic hash function
type HashFunc func(bytes []byte) uint

func FnvHash(bytes []byte) uint {
	hs := fnv.New64()
	hs.Write(bytes)
	return uint(hs.Sum64())
}

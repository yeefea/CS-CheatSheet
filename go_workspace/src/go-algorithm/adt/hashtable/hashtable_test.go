package hashtable

import (
	"strconv"
	"testing"
)

func TestNewHashTable(t *testing.T) {
	entrySize := 10
	ht := NewHashTable(entrySize)
	if ht.Size() != 0 {
		t.Error("size not 0")
	}
}

func TestFind(t *testing.T) {
	ht := NewHashTable(10)
	ht.describe()
	ht.Insert("123", 1)
	ht.describe()
	ht.Insert("124", 2)
	ht.describe()
	res, found := ht.Find("123")
	if !found {
		t.Error("key not found")
	}
	if res != 1 {
		t.Error("res incorrect")
	}
	res, found = ht.Find("124")
	if !found {
		t.Error("key not found")
	}
	if res != 2 {
		t.Error("res incorrect")
	}
	// update
	ht.Insert("124", 3)
	ht.describe()
	res, found = ht.Find("124")
	if !found {
		t.Error("key not found")
	}
	if res != 3 {
		t.Error("res incorrect")
	}

	res, found = ht.Find("125")
	if found {
		t.Error("nonexist key found")
	}
	if res != nil {
		t.Error("res is not nil")
	}
	ht.Delete("124")
	ht.describe()

	for i := 0; i < 18; i++ {
		ht.Insert(strconv.Itoa(i), i)
	}
	ht.describe()
}

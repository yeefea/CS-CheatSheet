package hashtable

import (
	"fmt"
	"go-algorithm/util/hashutil"
)

type listNode struct {
	Key   string
	Value interface{}
	next  *listNode
}

type HashTable struct {
	fnc     hashutil.HashFunc
	entries []listNode
	size    int
}

// NewHashTable HashTable factory
func NewHashTable(tableSize int) *HashTable {
	if tableSize < 1 {
		tableSize = 1
	}
	entries := make([]listNode, tableSize)
	return &HashTable{hashutil.FnvHash, entries, 0}
}

func (ht *HashTable) Size() int {
	return ht.size
}

func (ht *HashTable) Insert(Key string, val interface{}) {
	idx := ht.hash(Key)
	prev := &ht.entries[idx]
	entry := prev.next
	for entry != nil {
		if entry.Key == Key {
			entry.Value = val
			return
		}
		prev = entry
		entry = entry.next
	}
	prev.next = &listNode{Key, val, nil}
	ht.size++
	if ht.size*2 > len(ht.entries) {
		ht.rehash()
	}
}

func (ht *HashTable) Delete(Key string) (interface{}, bool) {
	idx := ht.hash(Key)
	prev := &ht.entries[idx]
	entry := prev.next
	for entry != nil {
		if entry.Key == Key {
			prev.next = entry.next
			ht.size--
			return entry.Value, true
		}
		prev = entry
		entry = entry.next
	}
	return nil, false
}

func (ht *HashTable) Exists(key string) bool {
	idx := ht.hash(key)
	entry := ht.entries[idx].next
	for entry != nil {
		if key == entry.Key {
			return true
		}
		entry = entry.next
	}
	return false
}

func (ht *HashTable) Find(Key string) (interface{}, bool) {
	idx := ht.hash(Key)
	entry := ht.entries[idx].next
	for entry != nil {
		if Key == entry.Key {
			return entry.Value, true
		}
		entry = entry.next
	}
	return nil, false
}

func (ht *HashTable) hash(key string) uint {
	return ht.getIdx(key, uint(len(ht.entries)))
}

func (ht *HashTable) getIdx(key string, nEntries uint) uint {
	res := ht.fnc([]byte(key)) % uint(nEntries)
	if res >= 0 {
		return res
	}
	return res + nEntries
}

func (ht *HashTable) rehash() {
	newLen := uint(len(ht.entries) * 2)
	newEntries := make([]listNode, newLen)
	for _, ent := range ht.entries {
		for ent.next != nil {
			tmp := ent.next
			idx := ht.getIdx(tmp.Key, newLen)
			ent.next = tmp.next
			newEnt := &newEntries[idx]
			tmp.next = newEnt.next
			newEnt.next = tmp
		}
	}
	ht.entries = newEntries
}

func (ht *HashTable) describe() {
	fmt.Println("***********Hash Table***********")
	for idx, entry := range ht.entries {
		fmt.Printf("%d ", idx)
		tmp := entry.next
		for tmp != nil {
			fmt.Printf("[%s : %v] -> ", tmp.Key, tmp.Value)
			tmp = tmp.next
		}
		fmt.Println("nil")
	}
	fmt.Println("********************************")
}

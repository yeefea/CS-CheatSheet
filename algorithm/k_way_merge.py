# from collections import heapq
from heapq import merge

def k_way_merge_builtin():
    l1 = [1, 4, 6, 100]
    l2 = [2, 5, 7]
    l3 = [3, 8, 9]
    print(list(merge(l1, l2, l3)))

def k_way_merge(*args):
    pass


if __name__ == '__main__':
    k_way_merge_builtin()

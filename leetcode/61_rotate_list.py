
class Solution:
    def rotateRight(self, head, k: int):
        if k < 1 or not head:
            return head
        n = 1
        end_node = head
        while end_node.next:
            n+= 1
            end_node = end_node.next
        if n == 1:
            return head
        k %= n
        if k == 0:
            return head
        ptr = head
        for _ in range(n-k-1):
            ptr = ptr.next
        new_head = ptr.next
        ptr.next = None
        end_node.next = head
        return new_head

if __name__ == '__main__':
    from util import print_linked_list, build_linked_list
    sol = Solution()
    res = sol.rotateRight(build_linked_list([]), 2)
    print_linked_list(res)
    res = sol.rotateRight(build_linked_list([1]), 2)
    print_linked_list(res)
    res = sol.rotateRight(build_linked_list([1,2]), 1)
    print_linked_list(res)
    res = sol.rotateRight(build_linked_list([1,2]), 2)
    print_linked_list(res)
    res = sol.rotateRight(build_linked_list([1,2,3,4,5]), 2)
    print_linked_list(res)
    res = sol.rotateRight(build_linked_list([1,2,3]), 20000000)
    print_linked_list(res)
    res = sol.rotateRight(build_linked_list([1,2,3,4,5]), 5)
    print_linked_list(res)
"""
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true

示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false

示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/same-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    """
    执行用时 :40 ms, 在所有 Python3 提交中击败了96.39% 的用户
    内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.10%的用户
    :param p:
    :param q:
    :return:
    """
    if bool(p) ^ bool(q):
        return False
    if p is None:
        return True
    return (p.val == q.val) and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

    一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7

返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4

返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balanced-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_balanced(root: TreeNode) -> bool:
    """
    二叉树后序遍历
    :param root:
    :return:
    """
    def check_node(node):
        if not node:
            return True, 0
        balance_left, h_left = check_node(node.left)
        balance_right, h_right = check_node(node.right)
        balance = abs(h_left - h_right) < 2
        return balance_left and balance_right and balance, max(h_left, h_right) + 1

    b, _ = check_node(root)
    return b

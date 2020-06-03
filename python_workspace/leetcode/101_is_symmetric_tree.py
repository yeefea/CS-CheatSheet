"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_symmetric_recursive(root: TreeNode) -> bool:
    """
    递归检查是否镜像对称
    :param root:
    :return:
    """
    def is_mirror(n1, n2):
        if bool(n1) ^ bool(n2):
            return False
        if n1 is None:
            return True
        return n1.val == n2.val and is_mirror(n1.left, n2.right) and is_mirror(n1.right, n2.left)

    return is_mirror(root, root)


def is_symmetric_iterative(root: TreeNode) -> bool:
    """
    层序遍历
    :param root:
    :return:
    """
    q = []
    q.extend([root, root])
    while q:
        n1 = q.pop(0)
        n2 = q.pop(0)
        if bool(n1) ^ bool(n2):
            return False
        if not n1:
            continue
        if n1.val != n2.val:
            return False
        q.append(n1.left)
        q.append(n2.right)
        q.append(n1.right)
        q.append(n2.left)
    return True

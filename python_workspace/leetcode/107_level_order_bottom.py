"""

"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def level_order_bottom(root: TreeNode) -> List[List[int]]:
    """
    层序遍历
    :param root:
    :return:
    """
    res = []
    current_layer = [root]  # 记录当前层的节点
    while current_layer:
        tmp_val = []
        next_layer = []  # 下一层的节点
        for node in current_layer:  # 遍历当前层
            if node:
                tmp_val.append(node.val)
                next_layer.extend([node.left, node.right])  # 将下一层节点放进列表
        if tmp_val:
            res.append(tmp_val)
        current_layer = next_layer
    res.reverse()  # 根据题目要求反转列表
    return res

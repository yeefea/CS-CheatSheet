from collections import deque


class BinaryNode:

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)


class BinaryTree:

    def __init__(self, root: BinaryNode):
        self.root = root

    def print_tree(self):
        """
        层序遍历并且打印二叉树
        """
        q = deque()
        q.append(self.root)
        n_last = self.root
        while len(q) > 0:
            n = q.popleft()
            is_last = bool(n_last == n)
            if is_last:
                print(n.value)
            else:
                print(n.value, end=' ')
            if n.left_child:
                q.append(n.left_child)
                if is_last:
                    n_last = n.left_child
            if n.right_child:
                q.append(n.right_child)
                if is_last:
                    n_last = n.right_child


def pre_order_traversal(node):
    """
    前序遍历
    :return:
    """
    lst = [node]
    if node.left_child:
        lst += pre_order_traversal(node.left_child)
    if node.right_child:
        lst += pre_order_traversal(node.right_child)
    return lst


def middle_order_traversal(node):
    lst = []
    if node.left_child:
        lst += middle_order_traversal(node.left_child)
    lst += [node]
    if node.right_child:
        lst += middle_order_traversal(node.right_child)
    return lst


def post_order_traversal(node):
    lst = []
    if node.left_child:
        lst += post_order_traversal(node.left_child)
    if node.right_child:
        lst += post_order_traversal(node.right_child)
    lst += [node]
    return lst


def level_order_traversal(node):
    lst = []
    q = deque()
    q.append(node)
    while len(q) > 0:
        n = q.popleft()
        lst.append(n)
        if n.left_child:
            q.append(n.left_child)
        if n.right_child:
            q.append(n.right_child)
    return lst


if __name__ == '__main__':
    node1 = BinaryNode(1)
    node2 = BinaryNode(2)
    node3 = BinaryNode(3)
    node4 = BinaryNode(4)
    node5 = BinaryNode(5)

    node1.left_child = node2
    node1.right_child = node3
    node2.left_child = node4
    node2.right_child = node5

    print(pre_order_traversal(node1))
    print(middle_order_traversal(node1))
    print(post_order_traversal(node1))
    print(level_order_traversal(node1))

    tree = BinaryTree(node1)
    tree.print_tree()




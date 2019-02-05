"""
https://en.wikipedia.org/wiki/Red%E2%80%93black_tree
1. Each node is either red or black.
2. The root is black. This rule is sometimes omitted. Since the root can always be changed from red to black, but not necessarily vice versa, this rule has little effect on analysis.
3. All leaves (NIL) are black.
4. If a node is red, then both its children are black.
5. Every path from a given node to any of its descendant NIL nodes contains the same number of black nodes.

https://zh.wikipedia.org/wiki/%E7%BA%A2%E9%BB%91%E6%A0%91
1. 节点是红色或黑色。
2. 根是黑色。
3. 所有叶子都是黑色（叶子是NIL节点）。
4. 每个红色节点必须有两个黑色的子节点。（从每个叶子到根的所有路径上不能有两个连续的红色节点。）
5. 从任一节点到其每个叶子的所有简单路径都包含相同数目的黑色节点。
"""
RED = 0
BLACK = 1


class RedBlackNode:

    def __init__(self, value, color=RED):
        self.value = value
        self.color = color
        self.parent = None
        self.left = None
        self.right = None

    def is_left_child_of_parent(self):
        if self.parent is None:
            return False
        if self.parent.left == self:
            return True
        return False

    def is_right_child_of_parent(self):
        if self.parent is None:
            return False
        if self.parent.right == self:
            return True
        return False

    def set_left_child(self, node):
        self.left = node
        if node is not None:
            node.parent = self

    def set_right_child(self, node):
        self.right = node
        if node is not None:
            node.parent = self

    def set_parent_left_child(self, parent):
        """

        :param parent:
        :return:
        """
        self.parent = parent
        if parent is not None:
            parent.left = self

    def set_parent_right_child(self, parent):
        self.parent = parent
        if parent is not None:
            parent.right = self

    @property
    def grandparent(self):
        if self.parent is None:
            return None
        return self.parent.parent

    @property
    def uncle(self):
        if self.parent is None:
            return None
        grandparent = self.grandparent
        if grandparent is None:
            return None
        if self.parent.is_right_child_of_parent():
            return grandparent.left
        else:
            return grandparent.right

    @property
    def sibling(self):
        if self.is_left_child_of_parent():
            return self.parent.right
        else:
            return self.parent.left

    def flip_color(self):
        if self.color == RED:
            self.color = BLACK
        else:
            self.color = RED

    def __repr__(self):
        return 'RedBlackNode({},{})'.format(self.value, self.color)

    def __str__(self):
        return '<{},{}>'.format(self.value, self.color)


_nil = RedBlackNode(None, BLACK)


class RedBlackTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = RedBlackNode(value, BLACK)
            self.root.left = _nil
            self.root.right = _nil
            return True
        else:
            return self._insert_value(self.root, value)

    def _insert_value(self, node, v):
        if v < node.value:
            if node.left == _nil:
                child = RedBlackNode(v)
                child.left = _nil
                child.right = _nil
                node.set_left_child(child)
                return self._insert_case(child)
            else:
                return self._insert_value(node.left, v)
        elif v > node.value:
            if node.right == _nil:
                child = RedBlackNode(v)
                child.left = _nil
                child.right = _nil
                node.set_right_child(child)
                return self._insert_case(child)
            else:
                return self._insert_value(node.right, v)
        else:
            return False

    def delete(self, value):
        if self.root is None or self.root == _nil:
            return False
        return self._delete_child(self.root, value)

    def contains(self, value):
        if self.root is None or self.root == _nil:
            return False
        return self._contain_value(self.root, value)

    def _contain_value(self, node, v):
        if v < node.value:
            if node.left == _nil:
                return False
            return self._contain_value(node.left, v)
        elif v > node.value:
            if node.right == _nil:
                return False
            return self._contain_value(node.right, v)
        elif v == node.value:
            return True
        else:
            return False

    @property
    def min(self):
        if self.root is None or self.root == _nil:
            return None
        return self._get_smallest_child(self.root).value

    @property
    def max(self):
        if self.root is None or self.root == _nil:
            return None
        return self._get_largest_child(self.root).value

    def _insert_case(self, node):
        """
        情形1:
        新节点N位于树的根上，没有父节点。在这种情形下，我们把它重绘为黑色以满足性质2。
        因为它在每个路径上对黑节点数目增加一，性质5匹配。
        情形2
        新节点的父节点P是黑色，所以性质4没有失效（新节点是红色的）。
        在这种情形下，树仍是有效的。性质5也未受到威胁，尽管新节点N有两个黑色叶子子节点；
        但由于新节点N是红色，通过它的每个子节点的路径就都有同通过它所取代的黑色的叶子的路径同样数目的黑色节点，所以依然满足这个性质。
        """
        # case 1
        if node.parent is None:
            node.color = BLACK
            return True
        # case 2
        if node.parent.color == BLACK:
            return True
        # case 3
        uncle = node.uncle
        if uncle.color == RED:
            node.parent.color = BLACK
            uncle.color = BLACK
            node.grandparent.color = RED
            return self._insert_case(node.grandparent)

        # case 4
        if node.is_right_child_of_parent() and node.parent.is_left_child_of_parent():
            self._rotate_left(node)
            node = node.left
        elif node.is_left_child_of_parent() and node.parent.is_right_child_of_parent():
            self._rotate_right(node)
            node = node.right

        # case 5
        node.parent.color = BLACK
        node.grandparent.color = RED
        if node.is_left_child_of_parent() and node.parent.is_left_child_of_parent():
            self._rotate_right(node.parent)
        else:
            self._rotate_left(node.parent)
        return True

    #
    # def _insert_case2(self, node):
    #     """
    #
    #     """
    #     if node.parent.color == BLACK:
    #         return True
    #     return self._insert_case3(node)
    #
    # def _insert_case3(self, node):
    #     uncle = node.uncle
    #     if uncle != _nil and uncle.color == RED:
    #         node.parent.color = BLACK
    #         uncle.color = BLACK
    #         node.grandparent.color = RED
    #         return self._insert_case(node.grandparent)
    #     else:
    #         return self._insert_case4(node)
    #
    # def _insert_case4(self, node):
    #     if node.is_right_child_of_parent() and node.parent.is_left_child_of_parent():
    #         self._rotate_left(node)
    #         node = node.left
    #     elif node.is_left_child_of_parent() and node.parent.is_right_child_of_parent():
    #         self._rotate_right(node)
    #         node = node.right
    #     return self._insert_case5(node)
    #
    # def _insert_case5(self, node):
    #     node.parent.color = BLACK
    #     node.grandparent.color = RED
    #     if node.is_left_child_of_parent() and node.parent.is_left_child_of_parent():
    #         self._rotate_right(node.parent)
    #     else:
    #         self._rotate_left(node.parent)
    #     return True

    def _delete_child(self, node, v):
        """
        从node和node的子节点中删除v
        :param node:
        :param v: value
        :return:
        """
        if node.value > v:  # node值 > v 要删除的节点在左子树里
            if node.left == _nil:
                return False  # 没找到要删除的节点，返回False
            return self._delete_child(node.left, v)
        elif node.value < v:  # node值 < v 要删除的节点在右子树里
            if node.right == _nil:
                return False  # 没找到要删除的节点，返回False
            return self._delete_child(node.right, v)
        elif node.value == v:
            if node.right == _nil:  # 右子树为空
                self._delete_one_child(node)  # 直接执行删除node节点的逻辑
                return True
            smallest = self._get_smallest_child(node.right)  # 查找右子树的最小节点
            self._swap_node_value(node, smallest)  # 交换node和smallest的值
            # 现在node的值在smallest里，删除smallest节点
            self._delete_one_child(smallest)
            return True
        # 这里是没用的
        return False

    def _delete_one_child(self, node):
        """
        前提条件: node最多只有一个子节点！
        :param node:
        :return:
        """
        if node.left is None:
            child = node.right
        else:
            child = node.left
        if node.parent is None and node.left is None and node.right is None:  # node是树中唯一的节点，删除根节点，树为空
            node = None
            self.root = node
            return

        if node.parent is None:  # node为根节点，删除后子节点变成根节点
            del node
            child.parent = None
            self.root = child
            self.root.color = BLACK
            return

        if node.is_left_child_of_parent():
            node.parent.set_left_child(child)
        else:
            node.parent.set_right_child(child)
        # child.parent = node.parent

        if node.color == BLACK:
            if child.color == RED:
                child.color = BLACK
            else:
                self.delete_case(child)
        del node

    def delete_case(self, node):
        """

        :param node:
        :return:
        """
        if node.parent is None:  # node 是 root节点
            node.color = BLACK  # node转黑，完成
            return

        # 此时node有父节点
        if node.sibling.color == RED:  # 兄弟节点是红的
            node.parent.color = RED  # 父节点转红
            node.sibling.color = BLACK  # 兄弟转黑
            if node.is_left_child_of_parent():  # 当前节点是左节点
                self._rotate_left(node.sibling)  # 兄弟节点左旋
            else:
                self._rotate_right(node.sibling)  # 兄弟节点右旋

        # 此时node的兄弟节点是黑的
        if node.parent.color == BLACK and \
                node.sibling.color == BLACK and \
                node.sibling.left.color == BLACK and \
                node.sibling.right.color == BLACK:  # 父节点、兄弟节点、兄弟的儿子都是黑的
            node.sibling.color = RED  # 兄弟转红
            self.delete_case(node.parent)  # 递归处理
        elif node.parent.color == RED and node.sibling.color == BLACK and \
                node.sibling.left.color == BLACK and node.sibling.right.color == BLACK:
            # 父节点是红的
            node.sibling.color = RED  # 兄弟转红
            node.parent.color = BLACK  # 父节点转黑
        else:

            if node.sibling.color == BLACK:
                if node.is_left_child_of_parent() and node.sibling.left.color == RED and \
                        node.sibling.right.color == BLACK:
                    node.sibling.color = RED
                    node.sibling.left.color = BLACK
                    self._rotate_right(node.sibling.left)
                elif node.is_right_child_of_parent() and node.sibling.left.color == BLACK and \
                        node.sibling.right.color == RED:
                    node.sibling.color = RED
                    node.sibling.right.color = BLACK
                    self._rotate_left(node.sibling.right)
                node.sibling.color = node.parent.color
                node.parent.color = BLACK
                if node.is_left_child_of_parent():
                    node.sibling.right.color = BLACK
                    self._rotate_left(node.sibling)
                else:
                    node.sibling.left.color = BLACK
                    self._rotate_right(node.sibling)

    @classmethod
    def _swap_node_value(cls, n1, n2):
        tmp = n1.value
        n1.value = n2.value
        n2.value = tmp

    def _rotate_left(self, node):
        """
        https://en.wikipedia.org/wiki/Tree_rotation
        
        before:
        gp
           \
             ft
           /    \
           1    node
                /  \
                2  3
        after:
        gp
           \
            node
           /    \
          ft     3
         /  \ 
        1    2   
        """
        if node.parent is None:
            self.root = node
            return
        gp = node.grandparent
        ft = node.parent
        y = node.left

        # right child of ft <- y
        ft.set_right_child(y)

        # left child of node <- ft
        node.set_left_child(ft)

        # check root node
        if self.root == ft:
            self.root = node

        # check grandparent node
        node.parent = gp
        if gp is not None:
            if gp.left == ft:
                gp.left = node
            else:
                gp.right = node

    def _rotate_right(self, node):
        """
        similar to _rotate_left
        """
        if node.parent is None:
            self.root = node
            return
        gp = node.grandparent
        ft = node.parent
        y = node.right
        ft.set_left_child(y)
        node.set_right_child(ft)
        if self.root == ft:
            self.root = node
        node.parent = gp
        if gp is not None:
            if gp.left == ft:
                gp.left = node
            else:
                gp.right = node

    @classmethod
    def _get_smallest_child(cls, node):
        while node.left != _nil:
            node = node.left
        return node

    @classmethod
    def _get_largest_child(cls, node):
        while node.right != _nil:
            node = node.right
        return node

    def __str__(self):
        return convert_red_black_node_to_str(self.root)


if __name__ == '__main__':
    from util.printing import convert_red_black_node_to_str

    rbtree = RedBlackTree()
    for n in range(10):
        rbtree.insert(n)

    print(convert_red_black_node_to_str(rbtree.root))

    for n in range(10):
        print(rbtree.delete(n))
        print(rbtree)
        print(rbtree.min)
        print(rbtree.max)
    print(rbtree.delete(1))
    print(rbtree)
    print(rbtree.min)
    print(rbtree.max)

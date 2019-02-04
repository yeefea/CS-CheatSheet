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

    def __init__(self, element=0, color=RED, left=None, right=None, parent=None):
        self.element = element
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

    @property
    def grandparent(self):
        if self.parent is None:
            return None
        return self.parent.parent

    @property
    def uncle(self):
        grandparent = self.grandparent
        if grandparent is None:
            return None
        if self.parent == grandparent.right:
            return grandparent.left
        else:
            return grandparent.right

    @property
    def sibling(self):
        if self.parent.left == self:
            return self.parent.right
        else:
            return self.parent.left
    
    def flip_color(self):
        if self.color == RED:
            self.color = BLACK
        else:
            self.color = RED


class RedBlackTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        pass
    
    def delete(self, value):
        pass
    
    def contains(self, value):
        pass

    def _insert_case1(self, node):
        """
        情形1:
        新节点N位于树的根上，没有父节点。在这种情形下，我们把它重绘为黑色以满足性质2。
        因为它在每个路径上对黑节点数目增加一，性质5匹配。
        """
        if node.parent is None:
            n.color = BLACK
        else:
            self._insert_case2(node)
    
    def _insert_case2(self, node):
        """
        情形2
        新节点的父节点P是黑色，所以性质4没有失效（新节点是红色的）。
        在这种情形下，树仍是有效的。性质5也未受到威胁，尽管新节点N有两个黑色叶子子节点；
        但由于新节点N是红色，通过它的每个子节点的路径就都有同通过它所取代的黑色的叶子的路径同样数目的黑色节点，所以依然满足这个性质。
        """
        if node.parent.color == BLACK:
            return
        self._insert_case3(node)

    def _insert_case3(self, node):
        """

        """
        uncle = node.uncle
        if uncle is not None and uncle.color == RED:
            node.parent.color=BLACK
            uncle.color = BLACK
            node.grandparent.color = RED
            self._insert_case1(node.grandparent)
        else:
            self._insert_case4(node)
    
    def _insert_case4(self, node):
        if node == node.parent.right and node.parent == node.grandparent.left:
            self._rotate_left(node.parent)
            node = node.left
        elif node == node.parent.left and node.parent == node.grandparent.right:
            self._rotate_right(node.parent)
            node = node.right
        self._insert_case5(node)

    def _delete_one_node(self, node):
        """
        """
        pass
        # todo

    def _insert_case5(self, node):
        node.parent.color = BLACK
        node.parent.color = RED
        if node == node.parent.left and node.parent == node.grandparent.left:
            self._rotate_right(node)
        else:
            self._rotate_left(node)

    def _delete_case1(self, node):
        pass
    
    def _delete_case2(self, node):
        pass
    
    def _delete_case3(self, node):
        pass    

    def _delete_case4(self, node):
        pass   

    def _delete_case5(self, node):
        pass    

    def _delete_case6(self, node):
        pass

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
        ft.right = y
        if y is not None:
            y.parent = ft
        
        # left child of node <- ft
        node.left = ft
        ft.parent = node
        
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
        ft.left = y
        if y is not None:
            y.parent = ft
        node.right = ft
        ft.parent = node
        if self.root == ft:
            self.root = node
        node.parent = gp
        if gp is not None:
            if gp.left == ft:
                gp.left = node
            else:
                gp.right = node

    
if __name__ == '__main__':

    n=RedBlackNode('test')
    print(n.color)


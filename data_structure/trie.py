class TrieNode:
    def __init__(self, end_of_word=False):
        self.end_of_word = end_of_word
        self.children = {}  # char -> TrieNode


class Trie:
    def __init__(self):
        self.size = 0
        self.root = TrieNode()

    def insert(self, word):
        is_new_word = False
        current_node = self.root
        for ch in word:
            tmp_node = current_node.children.get(ch)
            if tmp_node is None:
                tmp_node = TrieNode()
                current_node.children[ch] = tmp_node
                is_new_word = True
            current_node = tmp_node
        current_node.end_of_word = True
        if is_new_word:
            self.size += 1

    def is_empty(self):
        return self.size == 0

    def contains(self, word):
        current_node = self.root
        for ch in word:
            tmp_node = current_node.children.get(ch)
            if tmp_node is None:
                return False
            current_node = tmp_node
        return current_node.end_of_word

    def contains_prefix(self, prefix):
        """
        和contains的区别只有最后一行，contains需要判断是否是完整单词，这里不需要
        """
        current_node = self.root
        for ch in prefix:
            tmp_node = current_node.children.get(ch)
            if tmp_node is None:
                return False
            current_node = tmp_node
        return True

    def delete(self, word):
        """
        递归删除
        """

        def _delete(node, word, idx):  # -> bool(node can be deleted)
            if idx == len(word):
                if not node.end_of_word:
                    return False
                # word包含在trie中，删除，把end_of_words置为False
                node.end_of_word = False
                self.size -= 1
                return len(node.children) == 0  # 如果沒有children可以删除节点
            ch = word[idx]
            tmp_node = node.children.get(ch)
            if tmp_node is None:  # word不包含在trie中，什么都不用做
                return False
            can_delete = _delete(tmp_node, word, idx + 1)
            if can_delete:  # 删除多余的子节点
                del node.children[ch]
                return len(node.children) == 0

        _delete(self.root, word, 0)


if __name__ == "__main__":

    trie = Trie()
    trie.insert("test1")
    print(trie.size)
    trie.insert("test2")
    print(trie.size)
    trie.insert("test3")
    print(trie.size)
    trie.insert("test3")
    print(trie.size)
    print(trie.contains("test"))
    print(trie.contains_prefix("test"))
    print(trie.contains("test3"))
    print(trie.contains("pandas"))
    trie.delete("test3")
    print(trie.size)
    print(trie.contains("test3"))

class TrieNode:
    def __init__(self):
        self.is_leaf = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_leaf = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_leaf

    def has_children(self, node):
        return bool(node.children)

    def delete(self, node, word, depth=0):
        if node is None:
            return False

        if depth == len(word):
            if node.is_leaf:
                node.is_leaf = False
                return not self.has_children(node)
            return False

        char = word[depth]
        if char in node.children:
            should_delete = self.delete(node.children[char], word, depth + 1)
            if should_delete:
                del node.children[char]
                return not self.has_children(node) and not node.is_leaf

        return False

    def delete_word(self, word):
        self.delete(self.root, word)

trie = Trie()
words = ["apple", "banana", "grape", "orange", "watermelon"]
for word in words:
    trie.insert(word)

for word in words:
    print(f"'{word}' está na Trie?")
    if trie.search(word) == True:
        print("Sim, está na Trie \n")


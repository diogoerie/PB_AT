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

    def _delete(self, node, word, depth):
        if node is None:
            return None

        if depth == len(word):
            node.is_leaf = False
        else:
            char = word[depth]
            if char in node.children:
                node.children[char] = self._delete(node.children[char], word, depth + 1)

        if node.is_leaf:
            return node

        if any(node.children.values()):
            return node

        return None

    def delete_word(self, word):
        self.root = self._delete(self.root, word, 0)

    def simple_search(self, word):
        return self.search(word)

trie = Trie()
words = ["apple", "banana", "grape", "orange", "watermelon"]

for word in words:
    trie.insert(word)

for word in words:
    print(f"'{word}' está na Trie?")
    if trie.search("word") == True:
        print("Sim")
    else:
        print("Não")

trie.delete_word("banana")
print(f"'banana' está na Trie após exclusão?")
if trie.search("banana") == True:
    print("Sim")
else:
    print("Não")

from collections import defaultdict


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word: str) -> bool:

        def rec_search(word, node) -> bool:
            if not word:
                return node.isWord
            elif word[0] == ".":
                out = False
                for elem in node.children.values():
                    out = out or rec_search(word[1:], elem)
                return out
            elif word[0] in node.children:
                return rec_search(word[1:], node.children[word[0]])

        return rec_search(word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

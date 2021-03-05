class TrieNode(dict):
    def __init__(self, *args, **kwargs):
        self.end = False
        super(TrieNode, self).__init__(*args, **kwargs)


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for char in word:
            node = cur.get(char)
            if node is None:
                node = TrieNode()
                cur[char] = node
            cur = node
        cur.end = True

    def search(self, word):
        cur = self.root
        for char in word:
            cur = cur.get(char)
            if cur is None:
                return False
        return cur.end

    def startsWith(self, prefix):
        cur = self.root
        for char in prefix:
            cur = cur.get(char)
            if cur is None:
                return False
        return True


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                tree[a] = {}
            tree = tree[a]
        # 单词结束标志
        tree["#"] = "#"

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                return False
            tree = tree[a]
        if "#" in tree:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.lookup
        for a in prefix:
            if a not in tree:
                return False
            tree = tree[a]
        return True

trie = Trie();

trie.insert("apple")
trie.search("apple")   #// 返回 true
trie.search("app")     #// 返回 false
trie.startsWith("app") #// 返回 true
trie.insert("app")
trie.search("app")     #// 返回 true

"""
[208. 实现 Trie (前缀树)](https://leetcode-cn.com/problems/implement-trie-prefix-tree/)
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");   
trie.search("app");     // 返回 true
说明:

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。
***
说下代码里面 

tree[c] = { } #建立一个新的字典
tree =  tree[c] #进入tree[c]这个字典内部，相当于进入下一个节点
"""
```python
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
        for c in word:
            if c not in tree:
                tree[c] = {}
            tree = tree[c]
        #增加一个结束符
        tree['#'] = '#'


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.lookup
        for c in word:
            if c not in tree:
                return False
            tree = tree[c]
        if '#' in tree:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.lookup
        for c in prefix:
            if c not in tree:
                return False
            tree = tree[c]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

```

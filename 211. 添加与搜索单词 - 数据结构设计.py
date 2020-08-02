"""
[211. 添加与搜索单词 - 数据结构设计](https://leetcode-cn.com/problems/add-and-search-word-data-structure-design/)
设计一个支持以下两种操作的数据结构：

void addWord(word)
bool search(word)
search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。

示例:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
***
这道题主要是考查找单词，每次有三个状态。
- 为 " . "，可以任意匹配
- 为tree中存在的字符，然后tree = tree[c],进入下一个节点
- 不能匹配上，就返回Fasle

这里是采用的DFS的方法，这么做的好处就是结构清晰明了。
首先就是需要判断弹出条件，当word为空的时候，弹出。注意这里还需要判断是否匹配成功。

假如一个字符为 " .  ",那么这个字符对应很多个元素，我们应该对其可以匹配的所有下一个元素进行判断。
dict = ["abc", "adj", "asi"], 输入为 "a . x ",其中字符a可以匹配第一个，但是小数点可以匹配三个，如果使用for循环我们不好对其进行逐个的分析，所以使用递归的方法来实现。
"""
```python
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = {}


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        tree = self.tree
        for c in word:
            if c not in tree:
                tree[c] = {}
            tree = tree[c]
        tree['#'] = {}
        


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        # print(self.tree)

        def dfs(tree, word):
            if not word:
                if '#' in tree:
                    return True
                return False
            if word[0] in tree:
                if dfs(tree[word[0]], word[1:]):
                    return True
            elif word[0] == '.':
                for d in tree:#因为可能此次匹配多个字符，下一轮有多个待匹配的字符，使用for循环做不了
                    if dfs(tree[d], word[1:]):
                        return True
            return False

        return dfs(self.tree, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```

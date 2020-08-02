"""
[212. 单词搜索 II](https://leetcode-cn.com/problems/word-search-ii/)
给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

示例:

输入: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出: ["eat","oath"]
说明:
你可以假设所有输入都由小写字母 a-z 组成。

提示:

你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。
***
本题使用前缀树+回溯的方法：
有几个需要注意的地方：
- 集合不能使用add加入 （i，j） 类型，set.add((i,j))报错，可以使用或 set | {(i, j)}进行元素加入
- 我们在判断字符是否符合的时候，如果出现符合的字符，不能返回return，因为还有可能有其他更长的，前缀相同的字符串。
"""
```python
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.tree = {}

        for word in words:#构建前缀树字典
            tree = self.tree
            for c in word:
                if not c in tree:
                    tree[c] = {}
                tree = tree[c]
            tree['#'] = {}

        # print(self.tree)
        row = len(board)
        col = len(board[0])
        out = []

        def bakctrack(tree, res, used, i, j):#回溯算法
            if (i, j) in used: return
            if '#' in tree and res not in out:
                out.append(res)
                # return #不能提前终止，因为后面还可能有更长的字符，终止后结果会遗漏 
            if 0<=i<row and 0<=j<col and board[i][j] in tree:
                bakctrack(tree[board[i][j]], res+board[i][j], used|{(i,j)}, i+1, j)
                bakctrack(tree[board[i][j]], res+board[i][j], used|{(i,j)}, i-1, j)
                bakctrack(tree[board[i][j]], res+board[i][j], used|{(i,j)}, i, j+1)
                bakctrack(tree[board[i][j]], res+board[i][j], used|{(i,j)}, i, j-1)


        for i in range(row):
            for j in range(col):
                bakctrack(self.tree,'', set(), i, j)
        return out
```

[336. 回文对](https://leetcode-cn.com/problems/palindrome-pairs/)
给定一组唯一的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。

示例 1:

输入: ["abcd","dcba","lls","s","sssll"]
输出: [[0,1],[1,0],[3,2],[2,4]] 
解释: 可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
示例 2:

输入: ["bat","tab","cat"]
输出: [[0,1],[1,0]] 
解释: 可拼接成的回文串为 ["battab","tabbat"]
***
这道题不会啊。只有以后再看

```python3
# 修改 TrieNode 结构，用 index 替换 isEnd
from typing import List
class TrieNode:
    def __init__(self):
        self.index = -1
        self.children = {}
        self.palindromes = set()

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        root = TrieNode()
        res = []

        # 创建Trie
        for i in range(len(words)):
            self.addWord(root, words[i], i)
        

        # 利用Trie，找出所有的配对
        for i in range(len(words)):
            self.search(words, i, root, res)
        
        return res

    def isPalindrome(self, word, i, j):#判断是否是回文，这一段
        while i < j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        return True

    # 处理查找，从头遍历每个字符串，然后从Trie里寻找匹配的字符串
    def search(self, words, i, root, res):
        # k1 > k2，且 s1 剩下的字符能构成回文，就把这对组合添加到结果中
        # k1=k2 或 k1<k2，只需要把回文列表里的字符串都和 s1 组合即可
        for j in range(len(words[i])):
            if root.index >= 0 and root.index != i and self.isPalindrome(words[i], j, len(words[i])-1):
                res.append([i, root.index])
            if words[i][j] in root.children:
                root = root.children[words[i][j]]
            else:
                return

        for j in root.palindromes:
            if i != j:
                res.append([i, j])


    # 创建Trie的时候，从每个字符串的末尾开始遍历
    def addWord(self, root, word, index):
        for i in range(len(word)-1, -1, -1):
            ch = word[i]

            # 对于每个当前字符，如果它还没有被添加到children哈希表里，就创建一个新的节点
            if ch not in root.children:
                root.children[ch] = TrieNode()
            # 若该字符串从头开始到当前位置能成为回文的话，把这个字符串的下标添加到这个Trie节点的回文列表里
            if self.isPalindrome(word, 0, i):
                root.palindromes.add(index)

            root = root.children[ch]

        # 当对该字符串创建完Trie之后，将字符串的下标添加到回文列表里，并且将它赋给index
        root.palindromes.add(index)
        root.index = index
if __name__ == "__main__":
    s = Solution()
    print(s.palindromePairs(["abcd","dcba","lls","s","sssll"]))
```
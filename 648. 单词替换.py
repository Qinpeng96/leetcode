"""
[648. 单词替换](https://leetcode-cn.com/problems/replace-words/)
在英语中，我们有一个叫做 词根(root)的概念，它可以跟着其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。

现在，给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。

你需要输出替换之后的句子。

示例：

输入：dict(词典) = ["cat", "bat", "rat"] sentence(句子) = "the cattle was rattled by the battery"
输出："the cat was rat by the bat"
 

提示：

输入只包含小写字母。
1 <= dict.length <= 1000
1 <= dict[i].length <= 100
1 <= 句中词语数 <= 1000
1 <= 句中词语长度 <= 1000
***

 1. 建立一个字典树，通过循环插入每一个单词，以最后一 # 结尾
 2. 对句子中的单词以空格进行拆分
 3. 对每一个单词进行查看是否有词根
 4. 对单词中的每一个字符进行循环，如果字符在字典中就加入待替换的re_word
 5. 如果单词中的字符不在字典中的时候，我们就要弹出循环
 6. 弹出循环之后我们需要判断是否是已经找到截至的 # ，即是否已经找完一个字典后还有部分没有找到，比字典短，所以就算只能保持原始的单词字符 ，不能替换成为词根。
 7. 在循环的过程中，如果我们找到了一个 #，说明字典已经结束，单词比字典长，可以使用词根来替换，于是我们进行替换，然后将字典树在深入一步，弹出循环。
 8. 还有一种情况就是部分前缀相同，但是某一个字符和字典中的不一致，这个时候也需要弹出循环。这个时候肯定没有找到字典的结尾#，所以只能保留原始的字符，说明不匹配。

"""

```python
class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        self.tree = {}
        def insert(word):#插入一个word
            tree = self.tree
            n = len(word)
            for c in word:
                if c not in tree:
                    tree[c] = {}
                tree = tree[c]
            tree['#'] = '#'#结尾建立标志

        for word in dict:#将所有的单词都建立一个整体的字典树
            insert(word)
        # print(self.tree)

        words = sentence.split(' ')#分割句子中的单词

        res = []
        for word in words:
            tree  = self.tree
            re_word = ''
            for c in word:#寻找字典树
                if c in tree:
                    re_word += c
                    tree = tree[c]
                    if '#' in tree:#单词比字典长，找到字典的结尾，进行替换，深入一步字典，然后弹出
                        res.append(re_word)
                        tree = tree['#']
                        break
                else:#部分前缀相同，但是不匹配，不是词根，没能找到 #
                    break
            if '#' not in tree:#没有能够匹配上，或者单词比字典短，没能匹配上词根，保持原状
                res.append(word)

        return ' '.join(res)          
```

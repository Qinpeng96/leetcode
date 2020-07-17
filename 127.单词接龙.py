"""
[127. 单词接龙](https://leetcode-cn.com/problems/word-ladder/)
给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: 0

解释: endWord "cog" 不在字典中，所以无法进行转换。
***
其实就是将beginWord 单词作为树的根节点，依次向下遍历，看这棵树的叶子结点有没有endWord （有时候也不一定是叶子结点）。如果存在，返回其深度depth，反之返回0。此处有一点需要注意：

在树上层出现过的字符串没必要在下层再次出现，因为如果该字符串是转换过程中必须经过的中间字符串，那么应该挑选上层的该字符串继续进行变化，它的转换次数少。

因为题目所求的是最短转换序列的长度，所以一定要记住这一点。

另外还有一点就是这个转换规则：每次转换只能改变一个字母。每一次迭代中如何来找当前单词的转换单词呢？这里面所用的方法有很多种，我看了网上的一些帖子，大致分为两种。一种是将改变的字母按照小写字母排列情况分为26种情况，依次填进去进行判断。另一种是将改变字母的那个位置用“_”代替，比如“hit”要改变第二个位置的字母，则可表示为“h_t”，而“hot”改变第二个位置的字母后也可表示为“h_t”，说明这两个单词是可以直接转换的。


第一次尝试做一下，结果倒是正确，就是最后提交的时候结果超出了时间限制，那个测试例子是真的长 ∩=∩ ,还能怎么办，改呗。
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        num = len(beginWord)
        queue = collections.deque()
        queue.append(beginWord)
        used = []


        def is_valid(word, pattern):#判断待加入的单词是否符合加入条件：两者不等，只有一个字符不同
            count = 0
            if word == pattern and word != endWord:
                return False
            for i in range(num):
                if word[i] == pattern[i]:
                    count += 1
            if count >= num - 1:
                return True
            else:
                return False
            
        def solve( beginWord, endWord, wordList):#BFS，每一将符合条件的字符加入队列
            cnt = 1
            while queue:
                for _ in range(len(queue)):#本次队列有多少数，就循环多少次
                    node = queue.popleft()
                    used.append(node)#设置一个使用过的列表记录
                    
                    for item in wordList:
                        if is_valid(node, item) and item not in used and item not in queue:
                            if item == endWord:
                                return cnt+1
                            queue.append(item)
                            # print(queue)
                cnt += 1
            return 0

        return solve(beginWord, endWord, wordList)
"""
****
后来看了下题解，主要有两种方法解决超时问题

 1. 我们在单词匹配是否只差一个字母的时候用了太多的计算时间， dog, cog，只有中间一位不同，我们可以建立一个字典，其中 *og可以表示后两位位og的三位单词，这样做的话，以来就建立了一个字典，如果右只差一位的单词，就会被聚合到一个字典的键值下面。在进行BFS查找匹配的时候，我们的效率会加快很多
 2. 还有一种方法就是双向BFS,不止是单向从 begin 到 end, 我们也从 end 查找 begin，这个方法但是我现在还没仔细看，等下次回过头再看。

""""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS
        from collections import deque, defaultdict
        # 先验判断
        if endWord not in wordList:
            return 0
        # 提前构建邻接表 -> 用generic state做key
        intermidiateWords = defaultdict(list)
        wordLen = len(beginWord)
        for word in wordList:
            for i in range(wordLen):
                intermidiateWords[word[:i] + '*' + word[i+1:]].append(word)
        # 建队列 加初始状态
        queue = deque()
        memo = set()
        queue.append(beginWord)
        memo.add(beginWord)
        step = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                curWord = queue.popleft()
                for i in range(wordLen):
                    intermidiateCurWord = curWord[:i] + '*' + curWord[i+1:]
                    # 下一个状态的所有word
                    for word in intermidiateWords[intermidiateCurWord]:
                        if word == endWord:
                            return step + 1
                        if word not in memo:
                            queue.append(word)
                            memo.add(word)
            step += 1
        else:
            return 0

作者：cui-jin-hao-_official
链接：https://leetcode-cn.com/problems/word-ladder/solution/python-bfs-shuang-xiang-bfs-by-cui-jin-hao-_offici/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

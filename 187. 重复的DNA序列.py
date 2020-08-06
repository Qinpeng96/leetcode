"""
[187. 重复的DNA序列](https://leetcode-cn.com/problems/repeated-dna-sequences/)
所有 DNA 都由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来查找目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。

 

示例：

输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC", "CCCCCAAAAA"]
***
思路比较简单，就是从头开始每次取十个，看看是否在集合内，如果不在就加入集合，如果在就说明不是第一次出现了。
这个时候加入输出列表，注意，这里加入输出的时候需要去重。
"""
```python
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        dic = set()
        out = []
        for i in range(10, n+1):
            dna = s[i-10:i]
            if dna not in dic:#看是否在集合内
                dic.add(dna)
            else:
                if dna not in out:#加入输出的时候去重
                    out.append(dna)
        return out
```

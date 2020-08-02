"""
[677. 键值映射](https://leetcode-cn.com/problems/map-sum-pairs/)
实现一个 MapSum 类里的两个方法，insert 和 sum。

对于方法 insert，你将得到一对（字符串，整数）的键值对。字符串表示键，整数表示值。如果键已经存在，那么原来的键值对将被替代成新的键值对。

对于方法 sum，你将得到一个表示前缀的字符串，你需要返回所有以该前缀开头的键的值的总和。

示例 1:

输入: insert("apple", 3), 输出: Null
输入: sum("ap"), 输出: 3
输入: insert("app", 2), 输出: Null
输入: sum("ap"), 输出: 5
***
主要是访问键值球和那里，我开始使用的for循环进行求和，但是for 循环的时候，如果搜到了val,需要进行下一层的寻值，
就改变for的对象。但是由于是在循环中，改变for的对象就会出错，导致程序提前终止。

所以最后使用的是dfs，创建一个全局变量ans, dfs进行下一层的计算。
"""
```python
class MapSum:
    def __init__(self):
        self.d = {}

    def insert(self, key: str, val: int) -> None:
        t = self.d
        for c in key:
            if c not in t:
                t[c] = {}
            t = t[c]            #字典迭代
        t['val'] = val          #迭代终点赋值

    def sum(self, prefix: str) -> int:
        t = self.d
        for c in prefix:
            if c not in t:
                return 0        #判断前缀是否存在
            t = t[c]
        ans = 0
        def dfs(t):#使用DFS进行下一层的计算，如果用for循环实现不了
            for c in t:
                if c == 'val':
                    nonlocal ans
                    ans += t[c]
                else:
                    dfs(t[c])

        dfs(t)
        return ans
```

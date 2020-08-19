"""
[911. 在线选举](https://leetcode-cn.com/problems/online-election/)
在选举中，第 i 张票是在时间为 times[i] 时投给 persons[i] 的。

现在，我们想要实现下面的查询函数： TopVotedCandidate.q(int t) 将返回在 t 时刻主导选举的候选人的编号。

在 t 时刻投出的选票也将被计入我们的查询之中。在平局的情况下，最近获得投票的候选人将会获胜。

示例：

输入：["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
输出：[null,0,1,1,0,0,1]
解释：
时间为 3，票数分布情况是 [0]，编号为 0 的候选人领先。
时间为 12，票数分布情况是 [0,1,1]，编号为 1 的候选人领先。
时间为 25，票数分布情况是 [0,1,1,0,0,1]，编号为 1 的候选人领先（因为最近的投票结果是平局）。
在时间 15、24 和 8 处继续执行 3 个查询。
 

提示：

1 <= persons.length = times.length <= 5000
0 <= persons[i] <= persons.length
times 是严格递增的数组，所有元素都在 [0, 10^9] 范围中。
每个测试用例最多调用 10000 次 TopVotedCandidate.q。
TopVotedCandidate.q(int t) 被调用时总是满足 t >= times[0]。
***
以给的投票时间序列times为索引，记录每次投票后的胜出候选人，在查询的时候采用二分法即可在对数时间内返回正确结果。计算胜出候选人的时候，用hashmap记录每个候选人的票数，并用变量记录当前优胜者和最大票数，如果投票后，当前投给的候选人票数大于等于当前优胜者的票数，那么替换当前优胜者和最大票数。

首先我们需要计算出times时刻的优胜者是谁，然后对输入的t进行查找左边界，输出对应的优胜者。
***
代码：
"""
```python
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.n = len(times)
        self.times = times
        self.memo = {}
        self.win = [[] for _ in range(self.n)]
        dic = {}
        maxcnt = 0
        for i in range(self.n):#找到每一个时刻的优胜者是谁
            if persons[i] not in dic:
                dic[persons[i]] = 1
            else:
                dic[persons[i]] += 1
            if dic[persons[i]] >= maxcnt:#大于等于，因为票数相同，优胜者为最近的得票者
                maxcnt = dic[persons[i]]
                self.win[i] = persons[i]
            else:#优胜者没变
                self.win[i] = self.win[i-1]
        # print(self.win)

    def q(self, t: int) -> int:
        left, right = 0, self.n
        if t in self.memo:
            return self.memo[t]
        while left < right:#进行二人分查找
            mid = (left+right)//2
            if self.times[mid] == t:#找到时间后弹出
                left = mid+1
                break
            if self.times[mid] > t:
                right = mid
            else:
                left = mid + 1
        self.memo[t] = self.win[left-1]
        return self.memo[t]

        
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
```

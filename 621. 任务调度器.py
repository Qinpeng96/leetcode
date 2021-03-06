"""
[621. 任务调度器](https://leetcode-cn.com/problems/task-scheduler/)
给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。

然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的最短时间。

示例 ：

输入：tasks = ["A","A","A","B","B","B"], n = 2
输出：8
解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
     在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。 
 
提示：

任务的总个数为 [1, 10000]。
n 的取值范围为 [0, 100]。
***
分析一下题目：
冷却时间为n,我们有两种情况，一种是需要冷却，一种是交叉排布，不需要冷却的。
**我开始纠结了好久，需要冷却的情况我已经知道了，就是个数是频率最高的个数减一，再乘以冷却时间加一，最后再加上相同频率最高的个数。**
为什么是这样？举一个例子"AAAABBCC"。其中A=4，假如n=2,那么我们的排布就是
| AXX | AXX | AXX | A，这就是最少的排布，冷却为2，意思就是最少三个一组，最后一组可以不满。所以计算的公式为
$$ (nums[0] - 1) * (n+1) + cnt$$
频数为4，但是最后一个频数是没有装满的，每一组内的个数是冷却加一，所以是（n+1),最后加上的是最高频的个数，假如是AAAABBBBCC,那么最高频就为2个（AB),
 最佳的排列就是 ABXABXABX | AB，最后会多一组最高频的元数。所以这里就是cnt = 2.

**没有冷却等待的情况**：开始我想了很久，没有冷却等待我应该怎么进行排布？是不是应该每次都将次多的元数与最多的元数进行组合排布。这里排布的方法怎么写？
最后看了题解才知道，如果没有排布，那么就直接是任务数量相加的个数就是运行的次数，没有等待时间。

最后再无等待时间和有等待时间里面去一个最大值就行了，而不需要取想无等待的时候，怎么取才是最优的。这一点我之前没有跳出来。
"""



```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = {}#建立一个字典统计频率
        nums = []#将频数转化成一个列表
        cnt = 0#频率最高的相同个数
        for c in tasks:#创建一个频数字典，进行统计
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1
        for c in dic:
            nums.append(dic[c])
        
        length = sum(nums)#无需冷却，所有的任务都可以执行
        nums.sort(reverse = True)

        for i in range(len(nums)):
            if nums[i] == nums[0]:#计算最高频相同的个数
                cnt += 1
            else:
                break
        
        return max((nums[0]-1)*(n+1)+cnt, length)        
```

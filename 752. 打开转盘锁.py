"""
[752. 打开转盘锁](https://leetcode-cn.com/problems/open-the-lock/)
你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。
每个拨轮可以自由旋转：例如把 '9' 变为  '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。

锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。

列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。

字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。
示例 1:

输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
输出：6
解释：
可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
因为当拨动到 "0102" 时这个锁就会被锁定。
示例 2:

输入: deadends = ["8888"], target = "0009"
输出：1
解释：
把最后一位反向旋转一次即可 "0000" -> "0009"。
示例 3:

输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
输出：-1
解释：
无法旋转到目标数字且不被锁定。
示例 4:

输入: deadends = ["0000"], target = "8888"
输出：-1
***
锁盘有四个键，每一个键每一有两种变换的可能，所以个原始输入进去，会产生8个后续的变化可能。
但是我们有一个死区dead,和一个走过的数字visited。这两类内的数字就不能在实际产生并且加入到queue队列中。

下面是一种单向的BFS方法求解的过程：
"""
```python
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends: return -1
        queue = collections.deque()
        queue.append('0000')#加入队列
        visited = set() #建立一个集合，保存走过的路，防止往回走
        step = 1
        while queue:
            for i in range(len(queue)):#每次需要循环多少次
                cur = queue.popleft()
                for j in range(4):#由于有四个滑动键，每一个有两种变换(加减)
                    for k in [-1,1]:
                        tempcur = cur[:j] + str((int(cur[j])+k+10)%10) + cur[j+1:]
                        if tempcur not in deadends:
                            if tempcur == target: return step
                            if tempcur not in visited:
                                queue.append(tempcur)#没有走过，加入到队列
                                visited.add(tempcur)#加入走过的集合
            step += 1
        return -1
```
"""
这里我们还考虑是否能使用双向的BFS，因为双向的BFS的使用条件是，我们必须直到起始点和终点。有了这两个点的信息，
我们才能够双向的往中间靠，减少复杂度和计算时间。


双向BFS和单向BFS在程序上的区别就是，双向的BFS,我们设置的数据类型是list, list也可以左右pop。
其次，最重要的是：我们在每次遍历BFS的时候，我们都是遍历的queue, 每次结束遍历的的时候，我们queue2 - > queue，
**把目标列表赋值给起始列表，其实列表的下一批结果赋值给目标列表。**

这样做的目的就是，单次交叉BFS,减少中间过程产生的结果。并且每次都只循环一个列表，减少了程序的复杂度。
"""
```python
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends: return -1
        queue = []
        queue.append('0000')#加入队列
        deadends = set(deadends)
        queue2 = [target]
        visited = set() #建立一个集合，保存走过的路，防止往回走
        visited.add('0000')
        step = 1
        while queue and queue2:
            qlen = len(queue)
            tempset = []#设置本次queue的下一批可能节点，最后赋值给queue2，交叉BFS
            for i in range(qlen):#每次需要循环多少次
                cur = queue.pop(0)
                for j in range(4):
                    for k in [-1,1]:
                        tempcur = cur[:j] + str((int(cur[j])+k+10)%10) + cur[j+1:]
                        if tempcur not in deadends:
                            if tempcur in queue2: return step
                            if tempcur not in visited:
                                tempset.append(tempcur)#没有走过，加入到队列
                                visited.add(tempcur)#加入走过的集合
            step += 1
            queue = queue2#目标值queue2列表赋值给queue
            queue2 = tempset#本次queue的下一批节点赋值给queue2
        return -1
```

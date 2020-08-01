"""
[841. 钥匙和房间](https://leetcode-cn.com/problems/keys-and-rooms/)
有 N 个房间，开始时你位于 0 号房间。每个房间有不同的号码：0，1，2，...，N-1，并且房间里可能有一些钥匙能使你进入下一个房间。

在形式上，对于每个房间 i 都有一个钥匙列表 rooms[i]，每个钥匙 rooms[i][j] 由 [0,1，...，N-1] 中的一个整数表示，
其中 N = rooms.length。 钥匙 rooms[i][j] = v 可以打开编号为 v 的房间。

最初，除 0 号房间外的其余所有房间都被锁住。

你可以自由地在房间之间来回走动。

如果能进入每个房间返回 true，否则返回 false。

示例 1：

输入: [[1],[2],[3],[]]
输出: true
解释:  
我们从 0 号房间开始，拿到钥匙 1。
之后我们去 1 号房间，拿到钥匙 2。
然后我们去 2 号房间，拿到钥匙 3。
最后我们去了 3 号房间。
由于我们能够进入每个房间，我们返回 true。
示例 2：

输入：[[1,3],[3,0,1],[2],[0]]
输出：false
解释：我们不能进入 2 号房间。
***
这道题明显是使用BFS来做的，但是这道题的BFS和之前的有点不一样。主要是里面有一个套娃的操作。我们有门，门里又有钥匙，钥匙又对应门。。。。循环下去。

这道题还有一个细节就是visited保存的是门的信息，包括这次的门，和门中钥匙能开的下次门。但是queue中只包含的有本次门中钥匙下一次能开的不重复的门的信息。
所以我们这里需要分两次对之后的门信息进行保存。
"""

```python
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0]  
        start_key = []  
        queue = collections.deque()
        for key in rooms[0]:
            if key not in visited:
                visited.append(key)#加入的是走过的房间号
                for key1 in rooms[key]:
                    if key1 not in visited:
                        queue.append(key1)#queue里面是去过的房间里面的钥匙
                        visited.append(key1)

        while queue:
            num = queue.popleft()#弹出的是房间钥匙，如果钥匙对应的房间没有去过，则加入visited
            for key in rooms[num]:#房间内的钥匙可以打开的门
                if key not in visited:#没去过就加入visited
                    visited.append(key)
                    for key1 in rooms[key]:#房间内钥匙可以打开的房间里面的钥匙
                        if key1 not in visited:
                            queue.append(key1)
                            visited.append(key1)

        return True if len(visited) == len(rooms) else False
```
之后看了官方的题解，还有一些简便的方法：（我之前写的有点复杂了）

```python
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited, queue = {0}, [0]
        while queue:
            room_index = queue.pop()
            for key in rooms[room_index]:
                if key not in visited:
                    visited.add(key)
                    queue.insert(0,key)
        return len(visited) == len(rooms)

作者：qsctech-sange
链接：https://leetcode-cn.com/problems/keys-and-rooms/solution/7xing-dfs-8xing-bfs-liang-chong-fang-fa-san-chong-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

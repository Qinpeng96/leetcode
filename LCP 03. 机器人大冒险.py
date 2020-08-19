"""
[LCP 03. 机器人大冒险](https://leetcode-cn.com/problems/programmable-robot/)
力扣团队买了一个可编程机器人，机器人初始位置在原点(0, 0)。小伙伴事先给机器人输入一串指令command，机器人就会无限循环这条指令的步骤进行移动。指令有两种：

U: 向y轴正方向移动一格
R: 向x轴正方向移动一格。
不幸的是，在 xy 平面上还有一些障碍物，他们的坐标用obstacles表示。机器人一旦碰到障碍物就会被损毁。

给定终点坐标(x, y)，返回机器人能否完好地到达终点。如果能，返回true；否则返回false。


示例 1：

输入：command = "URR", obstacles = [], x = 3, y = 2
输出：true
解释：U(0, 1) -> R(1, 1) -> R(2, 1) -> U(2, 2) -> R(3, 2)。
示例 2：

输入：command = "URR", obstacles = [[2, 2]], x = 3, y = 2
输出：false
解释：机器人在到达终点前会碰到(2, 2)的障碍物。
示例 3：

输入：command = "URR", obstacles = [[4, 2]], x = 3, y = 2
输出：true
解释：到达终点后，再碰到障碍物也不影响返回结果。
 

限制：

2 <= command的长度 <= 1000
command由U，R构成，且至少有一个U，至少有一个R
0 <= x <= 1e9, 0 <= y <= 1e9
0 <= obstacles的长度 <= 1000
obstacles[i]不为原点或者终点
***
- 暴力法：计算出第一轮的轨迹之后，每一次迭代一轮，看是否有障碍在上面，看是否能够走到终点，如果此时的横纵坐标都大于终点，那么就返回False。
- 取余法：计算出第一轮的坐标，对终点和障碍的坐标取余，**注意：不能直接取余，需要先计算两者的倍数关系，选择最小额倍数关系相减取余数，因为这里的横纵坐标必须是同增的**
- 
"""

```python
from typing import List
#暴力迭代法，超时
class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        valid = False
        n = len(command)
        i, j = 0, 0
        track = []
        dis = [0,0]
        position = [0,0]
        # track.append(position[:])
        for c in command:
            if c == 'U':
                position[1] += 1
                track.append(position[:])
            elif c == 'R':
                position[0] += 1
                track.append(position[:])
        dis[0] = position[0]
        dis[1] = position[1]

        def nextTrack(track):
            nonlocal valid
            for i in range(n):
                track[i][0] += dis[0]
                track[i][1] += dis[1]
                if track[i] == [x, y]:
                    valid = True
                    return True
                if track[i] in obstacles or track[i][0] > x  or track[i][1] > y:
                    return False
            return True

        while not valid:
            if not nextTrack(track):
                return False
        return True
#取余数法
class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        valid = False
        n = len(command)
        track = [[0,0]]
        position = [0,0]

        for c in command:#初始化第一次轨迹
            if c == 'U':
                position[1] += 1
            elif c == 'R':
                position[0] += 1
            track.append(position[:])
		#计算终点的余数值，看是否在轨迹上
        times = min(x//position[0], y//position[1])
        i = x - times*position[0]
        j = y - times*position[1]

        if [i,j] not in track:
            return False
         #障碍为空，且终点在轨迹上，直接返回True
        if not obstacles:return True
		#对障碍取余数， 注意如果障碍值刚好等于终点，跳过计算
        for i,j in obstacles:
            if i <= x and j <= y and [i,j] != [x,y]:
                times = min(i//position[0], j//position[1])
                i = i - times*position[0]
                j = j - times*position[1]
                if [i,j] in track:
                    return False
        return True
        
if __name__ == "__main__":
    s = Solution()
    command = "URRU"
    obstacles = [[10, 5], [1, 6], [6, 10], [3, 0], [0, 3], [0, 10], [6, 2]]
    print(s.robot(command, obstacles, 7856,9033))        

```

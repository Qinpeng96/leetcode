"""
[1025. 除数博弈](https://leetcode-cn.com/problems/divisor-game/)
爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：

选出任一 x，满足 0 < x < N 且 N % x == 0 。
用 N - x 替换黑板上的数字 N 。
如果玩家无法执行这些操作，就会输掉游戏。

只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。

 

示例 1：

输入：2
输出：true
解释：爱丽丝选择 1，鲍勃无法进行操作。
示例 2：

输入：3
输出：false
解释：爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。
 
提示：

1 <= N <= 1000
***
这道题主要是在于分析找规律：
由于Alice先手：所以可以假设当前数字是ailice获胜的可能，为Ture or False;构造一个数组，找一下规律。

1: False		2:True		3:Fasle   这些是已知条件

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200724081738417.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
"""
```python
class Solution:
    def divisorGame(self, N: int) -> bool:
        if N % 2 == 0:return True
        else: return False
```

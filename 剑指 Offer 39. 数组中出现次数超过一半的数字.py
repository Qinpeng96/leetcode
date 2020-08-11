"""
[剑指 Offer 39. 数组中出现次数超过一半的数字数组中出现次数超过一半的数字](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/)
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

 

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1:

输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
 

限制：

1 <= 数组长度 <= 50000
***
看到一个网友说的非常好：

摩尔投票法：

核心就是对拼消耗。

玩一个诸侯争霸的游戏，假设你方人口超过总人口一半以上，并且能保证每个人口出去干仗都能一对一同归于尽。最后还有人活下来的国家就是胜利。

那就大混战呗，最差所有人都联合起来对付你（对应你每次选择作为计数器的数都是众数），或者其他国家也会相互攻击（会选择其他数作为计数器的数），但是只要你们不要内斗，最后肯定你赢。
***
采用一种对冲的思想；代码就孕育而生，采用投票，字典记录上一个数，但是我们可以不是用字典。

"""
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        dic = {}
        for num in nums:
            if not dic: #字典为空，加入字典，计数加一
                dic[num] = num
                count += 1
            elif num not in dic and dic:#字典不为空，并且是一个新的数，计数器减一，对冲
                count -= 1
                if count == 0:#如果计数器等于0 ，清空字典，重新开始
                    dic.clear()
            else:#本次加入的值就是之前的字典内的值
                count += 1
        for c in dic:
            return c
            

```
精简版本：

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote = 0
        for num in nums:
            if vote == 0:
                more = num
            vote += 1 if more == num else -1
        return more
```

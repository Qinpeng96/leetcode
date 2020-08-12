"""
[剑指 Offer 57 - II. 和为s的连续正数序列](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/)
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 

限制：

1 <= target <= 10^5
***
这道题使用滑动窗口的方法，起始我这里可以不建立数组，直接在满足条件的时候建立数组节约内存一些。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200812162252442.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center#pic_center)
- 当窗口的和小于 target 的时候，窗口的和需要增加，所以要扩大窗口，窗口的右边界向右移动
- 当窗口的和大于 target 的时候，窗口的和需要减少，所以要缩小窗口，窗口的左边界向右移动
- 当窗口的和恰好等于 target 的时候，我们需要记录此时的结果。设此时的窗口为 [i, j]，那么我们已经找到了一个 ii开头的序列，也是唯一一个 i 开头的序列，接下来需要找 i+1开头的序列，所以窗口的左边界要向右移动
"""

```python
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        left, right, n = 0, 1, (target+1)//2 + 1
        if n <= 2: return []
        nums = [i for i in range(1, n)]
        out = []
        # print(nums)
        res = nums[0] + nums[1]
        while True:

            if res == target:#等于目标值，加入输出，但是还是要尝试右移
                out.append(nums[left:right+1])
                right += 1
                if right < n-1:
                    res += nums[right]
                else:
                    break
                    
            elif res < target:#小于目标值，右移
                right += 1
                if right < n-1:
                    res += nums[right]
                else:
                    break
            else:#大于目标值，左移
                res -= nums[left]
                left += 1
        # print(out)
        return out
```
优化一下上面的代码：
看看大佬的

```python
def findContinuousSequence(self, target: int) -> List[List[int]]:
    i = 1 # 滑动窗口的左边界
    j = 1 # 滑动窗口的右边界
    sum = 0 # 滑动窗口中数字的和
    res = []

    while i <= target // 2:
        if sum < target:
            # 右边界向右移动
            sum += j
            j += 1
        elif sum > target:
            # 左边界向右移动
            sum -= i
            i += 1
        else:
            # 记录结果
            arr = list(range(i, j))
            res.append(arr)
            # 左边界向右移动
            sum -= i
            i += 1

    return res

作者：nettee
链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/shi-yao-shi-hua-dong-chuang-kou-yi-ji-ru-he-yong-h/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

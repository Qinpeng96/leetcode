"""
[42. 接雨水](https://leetcode-cn.com/problems/trapping-rain-water/)
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200819093145851.png#pic_center)
上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。
***
- 第一种方法是循环遍历的方法：
每次找到一个柱子，从其左右散开，寻找比其高的柱子的索引，找到之后，宽度就已经确定为两个索引之间的距离。此时的高度为两边边界柱子高度较小的那个减去当前索引的柱子高度。但是这种方法虽然能够解题，但是时间复杂度为O(n^2).
- 注意：由于寻找左右最高柱子，可以使用预处理，最后复杂度可达O(n).**每次计算的是该位置上方存储的水量**
代码如下：
"""
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        max_left[0] = height[0]
        max_right[-1] = height[-1]
        # 找位置i左边最大值
        for i in range(1, n):
            max_left[i] = max(height[i], max_left[i-1])
        # 找位置i右边最大值
        for i in range(n-2, -1, -1):
            max_right[i] = max(height[i], max_right[i+1])
        #print(max_left)
        #print(max_right)
        # 求结果
        res = 0
        for i in range(n):
            res += min(max_left[i], max_right[i]) - height[i]
        return res
```
"""
下面是来自[威威哥的解法](https://leetcode-cn.com/problems/trapping-rain-water/solution/bao-li-jie-fa-yi-kong-jian-huan-shi-jian-zhi-zhen-/)使用单调栈进行求解
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020081909550843.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
- 如果是一个单减的柱形高度，那么就不会存积雨水，例如上图的前几个。但是当出现不是递减的时候，例如下图，第5的位置出现一个高度比栈顶大的高度，那么说明此时出现了一个凹坑。
- 栈顶凹坑的积水等于左右比他高的柱子中的最小值减去当前栈顶的高度。宽度就是两者索引差减一。这样就得到了栈顶的积水量。
- 弹栈比较新的栈顶和待加入的柱子高度， 如果栈顶的高度还是小于与待加入的柱子高度，那么又可以计算出新栈顶的雨水量。如果该加入的高度小于新的栈顶高度，那么就入栈，因为不能形成凹坑接雨水。
- 



![在这里插入图片描述](https://img-blog.csdnimg.cn/20200819095228130.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
代码如下：
"""
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length < 3: return 0
        res, idx = 0, 0
        stack = []
        while idx < length:
            while len(stack) > 0 and height[idx] > height[stack[-1]]:
                top = stack.pop()  # index of the last element in the stack
                if len(stack) == 0:
                    break
                h = min(height[stack[-1]], height[idx]) - height[top]
                dist = idx - stack[-1] - 1
                res += (dist * h)
            stack.append(idx)
            idx += 1
        return res

作者：LotusPanda
链接：https://leetcode-cn.com/problems/trapping-rain-water/solution/xiong-mao-shua-ti-python3-shi-pin-jiang-jie-dan-di/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

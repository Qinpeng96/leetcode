"""
[347. 前 K 个高频元素347. 前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements/)
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
 

提示：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
你可以按任意顺序返回答案。
***
**十大排序算法的复杂度分析：**
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200803152156606.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)

下面使用的是建立字典，键值为数字，值为出现的次数。对出现的次数进行排序，取前K大的键值。
"""
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        out = []
        i = 0
        for c in nums:#建立字典
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1

        dic = sorted(dic.items(), key = lambda x: x[1], reverse = True)#对字典的所有值从大到小排序

        for c in dic:#取前K个最值加入输出
            out.append(c[0])
            i += 1
            if i == k: return out
```
"""
还有一种维护堆的方法：

```python
# 优先队列；n + nlogk， 时间复杂度： O(nlogk)
# 下面只从堆的角度考虑，从m个元素中，通过堆选出最大的k个数
# k大小的小根堆；堆满后，若新加的数大于堆首数，弹出堆首元素 -- 弹出了m-k个最小的
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq as hq
        lookup = Counter(nums)
        res = []
        heap = []
        for num, freq in lookup.items() :
            # 如果堆满了（k个元素）
            if len(heap) == k :
                # 弹出最小频率的元组
                if heap[0][0] < freq:
                    hq.heapreplace(heap, (freq, num))
            else : 
                hq.heappush(heap, (freq, num))
        while heap :
            res.append(hq.heappop(heap)[1])
        
        return res
"""
作者：yimingen
链接：https://leetcode-cn.com/problems/top-k-frequent-elements/solution/leetcode347onfu-za-du-bu-fen-si-xiang-ji-dui-jie-f/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
"""
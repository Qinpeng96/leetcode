"""
[632. 最小区间](https://leetcode-cn.com/problems/smallest-range-covering-elements-from-k-lists/)
你有 k 个升序排列的整数数组。找到一个最小区间，使得 k 个列表中的每个列表至少有一个数包含在其中。

我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。

示例 1:

输入:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
输出: [20,24]
解释: 
列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
注意:

给定的列表可能包含重复元素，所以在这里升序表示 >= 。
1 <= k <= 3500
-105 <= 元素的值 <= 105
对于使用Java的用户，请注意传入类型已修改为List<List<Integer>>。重置代码模板后可以看到这项改动。
***
这道题目我首先想到的就是[76. 最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/)这道题的解法，
使用滑动窗口进行求最小包含区间。但是这道题目在原始的数据中是多个列表的存在形式。所以在确定每一个列表都有一个值得时候，需要对每一个列表增加一个列表属性的标签。

增加属性标签就是将一维的列表增至二维，第一维为属性，第二维为数值。再将每一组二维数据合并在一起，具体的实现代码为：
#
        for i in range(k):#k个列表
            res += [[i, item] for item in nums[i]]#对每一个列表的内的数组增维


增维之后我们再对数据的第二维进行一个递增排序，这样就和之前的76题类似了。

 1. 建立两个字典，一个为目标需要的字典need,包含了key,val。key:需要的标签名称，val:该类标签需要的个数。
    由于本次需要所有的k个列表内的值，都出现依次，所以可以直接复制，key = i , val = 1。
 2. 建立win窗口字典，包含的是窗口内的标签种类以及数量。当win满足need的最低要求时，可以加入输出。这里的最低要求使用的是valid表示，
    每当win[i] 增加一个之后，win[i] == 1,的时候，valid就会加一，之后win[i]再继续增加，超过一，虽然会继续计数，但是valid值是不会增加，因为已经满足最小匹配了。
 3. 当valid 的个数等于 k的个数的时候，说明这个区间内是满足至少每个列表有一个数的。为了求一个最优的区间，这个时候需要缩小左边界。
    缩小左边界的时候，如果最左边对应的字典值win[ i ]  == 1,那么在缩小的过程中间，win[ i ] 就会变成0，此时的valid个数也会减一。
 4. 每次得到valid == k的时候，我们要计算一下此时的区间长度，每次更新找到一个最优的区间长度。
"""
```python
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        if not nums: return []
        res = []
        need = {}
        win = {}
        valid = 0
        sec = 0
        k = len(nums)        
        left, right = 0, 0
        section = float('inf')

        for i in range(k):#升维，变化为二维
            res += [[i, item] for item in nums[i]]

        res.sort(key = lambda x: x[1])#对第二个值进行从小到大的排序
        # print(res)
        length = len(res)

        for i in range(k):#创建一个need字典
            # if i not in need:
            need[i] = 1
        
        while right < length:#当还有字符没有判断时
            c = res[right]#获得待加入的字符
            right += 1#光标右移
            if c[0] not in win:#如果该字符的标签不在win中，就加入进来，否则对应的value加一
                win[c[0]] = 1
            else:
                win[c[0]] += 1
            if win[c[0]]  == need[c[0]]:#当某一个key的个数为1就把valid加一
                valid += 1

            while valid == k:#每个列表内的数都有被包含的时候
                if res[right-1][1] - res[left][1] < section:#如果长度更短
                    section = res[right-1][1] - res[left][1]#更新长度
                    sec = right - 1 - left#更新索引坐标
                    start = left#更新起始位置
                
                d = res[left]#待缩小的左边界的值
                left += 1
                if win[d[0]] == 1:#如果缩小的左边界的值的value小于1，那么valid就要减一
                    valid -= 1
                win[d[0]] -= 1
                
        return [res[start][1], res[start+sec][1]] if section != float('inf') else []
```

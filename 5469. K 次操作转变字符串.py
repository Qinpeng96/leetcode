"""
[5469. K 次操作转变字符串](https://leetcode-cn.com/problems/can-convert-string-in-k-moves/)
给你两个字符串 s 和 t ，你的目标是在 k 次操作以内把字符串 s 转变成 t 。

在第 i 次操作时（1 <= i <= k），你可以选择进行如下操作：

选择字符串 s 中满足 1 <= j <= s.length 且之前未被选过的任意下标 j （下标从 1 开始），并将此位置的字符切换 i 次。
不进行任何操作。
切换 1 次字符的意思是用字母表中该字母的下一个字母替换它（字母表环状接起来，所以 'z' 切换后会变成 'a'）。

请记住任意一个下标 j 最多只能被操作 1 次。

如果在不超过 k 次操作内可以把字符串 s 转变成 t ，那么请你返回 true ，否则请你返回 false 。

 

示例 1：

输入：s = "input", t = "ouput", k = 9
输出：true
解释：第 6 次操作时，我们将 'i' 切换 6 次得到 'o' 。第 7 次操作时，我们将 'n' 切换 7 次得到 'u' 。
示例 2：

输入：s = "abc", t = "bcd", k = 10
输出：false
解释：我们需要将每个字符切换 1 次才能得到 t 。我们可以在第 1 次操作时将 'a' 切换成 'b' ，但另外 2 个字母在剩余操作中无法再转变为 t 中对应字母。
示例 3：

输入：s = "aab", t = "bbb", k = 27
输出：true
解释：第 1 次操作时，我们将第一个 'a' 切换 1 次得到 'b' 。在第 27 次操作时，我们将第二个字母 'a' 切换 27 次得到 'b' 。
 

提示：

1 <= s.length, t.length <= 10^5
0 <= k <= 10^9
s 和 t 只包含小写英文字母
***

 - 首先计算字符串对应的序号差值，如果差值为负数，那么差值要加上26
 - 计算好两个字符串对应的每一个键的差值之后进行相同数值的统计
 - 如果某一个次数为2，例如dic[1] = 2，那么第一次转动1，第27次(1+26)转动27，就可以满足
 - 所以我们寻找一个最大的次数cnt,如果cnt < k，那么说明可以完成。

** 注意，每次重复转动的数值都要增加26.表示多一圈又转到原始位置。**
"""
```python
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        m = len(t)
        if n != m: return False
        nums = [0]*n
        for i in range(n):#计算两个字符床的差值（负数+26）
            temp = ord(t[i]) - ord(s[i])
            if temp >= 0:
                nums[i] = temp
            else:
                nums[i] = 26+temp
        # print(nums)
        do = max(nums)#其中最大的次数
        #预处理一下
        if do > k:return False
        
        dic = {}#建立一个字典，将次数不为0的统计频次
        cnt = 0
        for i in range(n):
            if nums[i]!= 0:
                if nums[i] not in dic:
                    dic[nums[i]] = 1
                else:
                    dic[nums[i]] += 1
                    if nums[i] != 0:
                        cnt += 1

        count = 0#统计完频次之后，就选择一个最多的转动次数和k进行比较
        for c in dic:
            count = 26*(dic[c]-1)+c
            if count > k:
                # print('ok')
                return False
           
        return True
```
偷一偷肖总的代码：

```python
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        
        if len(s)!= len(t):
            return False
        
        has_oper = [0]*26 
        n = len(s)
        
        for i in range(n):
            a = ord(s[i])
            b = ord(t[i])
            if a != b:
                cnt = b-a if a < b else 26-(a-b)
                check = False
                if has_oper[cnt-1]*26 + cnt <= k: #可以切换
                    has_oper[cnt-1] += 1
                    check = True
                if not check:
                    return False
        return True

作者：2547892696
链接：https://leetcode-cn.com/problems/can-convert-string-in-k-moves/solution/python3-shuang-bai-by-2547892696/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

"""
[321. 拼接最大数](https://leetcode-cn.com/problems/create-maximum-number/)
给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。
现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。

求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。

说明: 请尽可能地优化你算法的时间和空间复杂度。

示例 1:

输入:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
输出:
[9, 8, 6, 5, 3]
示例 2:

输入:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
输出:
[6, 7, 6, 0, 4]
示例 3:

输入:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
输出:
[9, 8, 9]
***
这道题和之前的[316. 去除重复字母](https://leetcode-cn.com/problems/remove-duplicate-letters/)类似，
只不过之前的题目要求的是一个最小值，这里变成了一个最大值。并且这里是对两个数组进行取值。

 1. 由于有两个列表，都可以取值。当所需取得个数为k的时候，从第一个列表可取 i 个，则第二个列表可以  k - i 个。
    注意在取值的时候，我们的输入 pick_max(nums, k)的k是所需要取得个数，加入一个nums长度为2, 那么我们的输入 k 最多为2。
    因此需要对输入pick_max的长度k进行限制。
 2. 两个列表所取总的个数为k,在对两个列表进行总循环的时候，我们for内的值应该是(k+1),这样才能取到长度 k。
 3. 在pick_max内，我们的stack不需要以来就赋值，因为在循环中我们在栈为空的情况下，while循环不成立，所以会有一个入栈的操作。
 4. 最后就是找到了两个列表所取得不同长度得最大列表后怎么进行组合得问题。我们知道python 中列表之间得大小比较是根据
    第一位数来确定得，所以我们可以直接对两个列表作比较，取出两者之间得较大值。
 5. **注意** ==列表的赋值是一个引用的过程==，所以我们对得到的较大列表不用管他是谁，将第一个数字加入输出之后，
    直接pop第一个数字就可以了进行下一步比较了。最后取出一个组大的组合即可。

***
"""
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick_max(num, k):#从列表中找到最大的k个数组合（不改变位置）
            n = len(num)
            drop = n - k#计算需要丢弃的数字个数
            stack = []
            for i in range(n):#对之后的每个数进行比较
                while drop and stack and num[i] > stack[-1]:#待加入的值比栈顶的值大，则栈顶弹出，丢弃值减一
                    stack.pop()
                    drop -= 1
                stack.append(num[i])#入栈
            return stack[:k]#输出需要的长度，因为列表可能是递减的

        def merge(num1, num2, k):
            out = []
            m, n = len(num1), len(num2)
            for i in range(k+1):#每个组中循环取 0-k共k+1个数
                if i <= m and k-i <= n:#注意这里必须对循环的索引进行限制，非则会越界
                    res = []
                    res1 = pick_max(num1, i)#得到列表1中的最大子列表
                    res2 = pick_max(num2, k-i)#得到列表2中的最大子列表
                    print(res1, res2)
                    while res1 or res2:#开始合并，当两者都为空的时候才停止
                        ans = res1 if res1 > res2 else res2#两个子列表的中较大的一个赋给ans,这里是引用
                        res.append(ans[0])#本次输出res,连接较大列表的首个数字，之后再弹出
                        ans.pop(0)#这里的ans弹出左边的值，也等于res1或者res2中较大的一个弹出左值，因为列表为引用
                    out = max(out, res)  #对所有的组合中去一个最大的作为输出
            return out  
        return merge(nums1, nums2, k)

                    




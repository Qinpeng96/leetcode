"""
[402. 移掉K位数字](https://leetcode-cn.com/problems/remove-k-digits/)
给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。

注意:

num 的长度小于 10002 且 ≥ k。
num 不会包含任何前导零。
示例 1 :

输入: num = "1432219", k = 3
输出: "1219"
解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
示例 2 :

输入: num = "10200", k = 1
输出: "200"
解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
示例 3 :

输入: num = "10", k = 2
输出: "0"
解释: 从原数字移除所有的数字，剩余为空就是0。
****

 1. 首先计算出最终会有多少个保留的数
 2. 如果待加入的数小于栈顶的数，就弹栈，在弹栈的时候，待删除的数的数量减一
 3. 如果是递增的，或者已经没有要删除的数了，那么直接加入栈中。
 4. 最后输出栈中的元数，并且将左边的0去掉，如果去掉左0之后为空则返回 ‘0’
==**注意**：可能没有那么多需要删除的数字，例如数组是一个递增的数组，那么我们就取前面的位次。==
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not num: return '0'
        n = len(num)
        if n == k: return '0'
        remain = n - k#计算最终列表中会有多少个元素，取前面的多少位
        stack = [num[0]]

        for i in range(1, n):
            while stack and num[i] < stack[-1] and k:#栈顶元数大于待加入的元数，并且还能弹出，则弹栈
                stack.pop()
                k -= 1
            stack.append(num[i])#直到不能弹栈就入栈，这会导致之后元数都会入栈
        print(stack)
        return ''.join(stack[:remain]).lstrip('0')  or '0'#如果输出为空，则输出0     


"""
[1081. 不同字符的最小子序列](https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters/)
返回字符串 text 中按字典序排列最小的子序列，该子序列包含 text 中所有不同字符一次。

 示例 1：

输入："cdadabcc"
输出："adbc"
示例 2：

输入："abcd"
输出："abcd"
示例 3：

输入："ecbacba"
输出："eacb"
示例 4：

输入："leetcode"
输出："letcod"
 

提示：

1 <= text.length <= 1000
text 由小写英文字母组成
***
这道题和之前的[316. 去除重复字母](https://leetcode-cn.com/problems/remove-duplicate-letters/)
是一模一样的，这里就不赘述了。
"""

class Solution:
    def smallestSubsequence(self, text: str) -> str:
        n = len(text)
        stack = []
        for i in range(n):
            if text[i] not in stack:
                while stack and stack[-1] > text[i] and stack[-1] in text[i+1:]:
                    stack.pop()
                stack.append(text[i])
        return ''.join(stack)


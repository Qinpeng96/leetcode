"""
题目：
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

*********************************************************

算法推导
使用动态规划，由于之后的（）与之前的（）个数有关，所以可以考虑使用 DP
特判，若ss为空，返回00

初试化dp=[0,...,0]，长度为n。dp[i]表示到i位置的最长有效括号的长度。
显然，当s[i]为((时，dp[i]=0

遍历字符串，遍历区间[1,n)：

当s[i]==)时，若s[i-1]==(，说明这两个有效。则dp[i]=dp[i-2]+2
否则s[i-1]==)，此时找到上一匹配字符串的上一位i-dp[i-1]-1：
若s[i-dp[i-1]-1]==(，说明s[i]可以和s[i-dp[i-1]-1]匹配：则dp[i]=dp[i-1]+dp[i-dp[i-1]-2]+2，
表示当前位置的最长有效括号长度等于上一位有效括号的长度加上自身匹配的上一位的有效括号的长度加上2。
更新res，res=max(res,dp[i])
返回res

作者：wu_yan_zu
链接：https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zhan-dong-tai-gui-hua-zhu-xing-jie-shi-dai-ma-pyth/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""
from typing import List
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        input_list = list(s)
        len_s = len(s)
        dp = [0]*len_s#初始化动态空间 0，记录的是每个角标之前的最长有效括号长度
        res = 0 #最长有效括号
        if len_s < 2: return 0
        for i in range(1, len_s):#从第一个位置开始匹配
            if s[i] == ')':#遇到右括号
                if s[i-1] == '(' and s[i] == ')':#如果和前一个左括号匹配
                    dp[i] = dp[i-2] + 2#该位置的dp内的值等于往前数2个位置的dp内的值
                #如果s[i-1]=s[i]=),即连续的两个右括号，则如果s[i-1]前dp[i-1]个符号是（，则可以匹配
                if (s[i-1] == ')' and s[i-1-dp[i-1]] == '(' and i-1-dp[i-1] >= 0):
                    #此时dp[i]等于两端dp,即dp[i-1]和s[i]匹配的（之前的有效长度dp[i-1-dp[i-1]-1]所含的有效括号
                    #再加上本次匹配的（），值为2
                    dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
                res = max(res, dp[i])#返回每次dp中最大的值
        return res

if __name__ == "__main__":
    input_num = ")()(()))"
    # input_num ="()(()"
    solution = Solution()
    output = solution.longestValidParentheses(input_num)
    print(output)

"""
*********************************************************

算法推导
使用栈，每次如果输入是')'，前一个为'('，则pop出栈
1.特判，若s为空，返回0

2.初试化栈stack=[-1]，和结果res=0。栈中元素表示上一不匹配位置索引。

3.遍历s[]：

若s[i]=="("，将当前位置索引加入stack。表示将当前左括号需要匹配，为不匹配索引。
若s[i]==")"：
出栈，stack.pop()。表示将对应左括号索引出栈，或者当栈中只有))时，将上一)索引出栈。
若栈为空，表示之前的所有的(匹配成功，上一步出栈的是栈底的-1或者是前一个不匹配的)。则更新栈底为当前)的索引，表示不匹配的位置。
否则，说明和栈中的(匹配上了，此时更新最长序列res=max(res,i-stack[-1])。表示当前位置索引减去上一不匹配位置索引 和之前res中的较大值。

作者：wu_yan_zu
链接：https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zhan-dong-tai-gui-hua-zhu-xing-jie-shi-dai-ma-pyth/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if(not s):
            return 0
        #即假设第一个不匹配的地方位于-1
        stack=[-1]#这里初试栈为-1值，假如（），则）为1，1-（-1）等于2
        res=0
        for i in range(len(s)):
            if(s[i]=="("):#每次将左括号的坐标入栈
                stack.append(i)
            else:
                stack.pop()#每次遇见右括号，则将上一个栈内的值出栈，因为只有左括号入栈，所以出栈的都是左括号[-1除外]
                if(not stack):#栈为空，即第一个栈内的-1被pop,即输入的是)，且没有与之匹配的（，所以）为不匹配点，加入栈
                    stack.append(i)
                else:#代表了进行了一次（）pop,所以计算本次角标与上一次不匹配点的角标差值极为最长有效括号
                    res=max(res,i-stack[-1])#返回最大的有效括号长度
        return res

if __name__ == "__main__":
    input_num = ")()(()))"
    # input_num ="()(()"
    solution = Solution()
    output = solution.longestValidParentheses(input_num)
    print(output)
"""
作者：wu_yan_zu
链接：https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zhan-dong-tai-gui-hua-zhu-xing-jie-shi-dai-ma-pyth/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""
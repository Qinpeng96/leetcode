"""
44. 通配符匹配
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
示例 3:

输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:

输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例 5:

输入:
s = "acdcb"
p = "a*c?b"
输出: false
"""
from typing import List
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
      len_p = len(p)
      len_s = len(s)
      memo = {}
      def dp(i,j):
        if j == len_p:return i == len_s
        if (i, j) in memo: return memo[(i, j)]#在字典中进行查找
        if i < len_s and p[j] in {s[i], '?','*'}:#单个匹配情况
          first_match = True
        elif i == len_s and p[j] == '*':#如果s匹配完，但是p还有 * 
          first_match = True
        else:#单个字符不匹配
          first_match = False

        if j < len_p-1 and p[j] == '*':#p中为*，则要么使用，要么不使用为空
          ans = first_match and (dp(i+1,j) or dp(i,j+1))
        elif j == len_p-1 and p[j] == '*':#此时假如p的最后一个为*，则不用再递归，直接返回True
          ans = first_match
        else:#其他情况，两者都后移一位，进行判断
          ans = first_match and dp(i+1,j+1)

        memo[(i, j)] = ans #加入字典
        return ans
      return dp(0,0)
if __name__ == "__main__":
    s = Solution()
    print(s.isMatch("mississippi", "*mis*"))




    

"""
10. 正则表达式匹配
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false

"""
"""
from typing import List
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
      if not p: return not s #匹配完成，或者p被匹配完，看s是否还有未匹配的
      #两个字符当前位是否匹配或着p中当前位为 '*'的情况
      first_match = True if s and (p[0] in {s[0], '.'}) else False
      #当p的当前为'*'号时，可以匹配0次或者无穷次，但是是要和前一个字符相同，所以要两个字符进行判断
      if len(p) > 1 and p[1] == '*':
        return (self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p)))
      else:
        return first_match and self.isMatch(s[1:], p[1:])
"""
#dp[i][j] 表示的状态是 s 的前 i 项和 p 的前 j 项是否匹配。
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
      memo = {}
      def dp(i, j):
        if (i, j) in memo: return memo[(i, j)]#查找记录在字典里面的值
        if j == len(p): return i == len(s)
		#对第一个首字符进行判断
        first_match = True if i < len(s) and p[j] in {s[i], '.'} else False
		#当p的当前为'*'号时，可以匹配0次或者无穷次，但是是要和前一个字符相同，所以要两个字符进行判断
        if j < len(p)-1 and p[j+1] == '*':
          ans = dp(i, j+2) or (first_match and dp(i+1, j))
        else:
          ans = first_match and dp(i+1,j+1)
        memo[(i, j)] = ans#写入字典
        return ans#返回值 Fasle or True
      return dp(0,0)

if __name__ == "__main__":
  s = Solution()
  print(s.isMatch("mississippi","mis*is*ip*."))

    

"""
91. 解码方法
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
"""
from typing import List

#递归方法
class Solution:
    def numDecodings(self, s: str) -> int:
        out = []
        nums = list(s)
        n = len(s) 

        def uncode(s, index):
            if len(s) == 0:
                out.append(1)
                return 
            for i in range(index, n):
                if i< n-1 and s[0] != '0' and (0 < (int(s[0])*10 + int(s[1])) <= 26):
                    uncode(s[2:], i+2)
                if int(s[0]) > 0:
                    uncode(s[1:], i+1)
                return 

        uncode(nums,0)
        return(len(out))

#动态规划，整理四种条件
class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s) 
        dp = [0] * (n+1)
        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1
        else:
            return 0
        

        for i in range(1,n):
            if s[i] == '0' and s[i-1] in {'1', '2'}:#为双编码的情况此时为 10 20两种情况
                dp[i+1] = dp[i-1]
            elif '0' < s[i-1:i+1] <= '26' and s[i-1] != '0':#此时为 [1,26]的情况，这种情况可以两个编码，也可以逐个编码
                dp[i+1] = dp[i-1] + dp[i]
            elif s[i-1:i+1] > '26'and s[i] != '0':#s[2] > 26,并且s[i] != 0，即35，28，73等，只能依次逐个编码
                dp[i+1] = dp[i]
            elif s[i-1] == '0'and s[i] != '0':#此时为 01，09，02等，前一个为0，后一个不为0的情况，前一个为0，说明肯定可编码组合，
                dp[i+1] = dp[i]#应该是10，20 已经组合过了，s[i] = 0，就不能被编码，所以只能为大于0的数字
            else:
                return 0
        return(dp[-1])


#动态规划，进行条件的整合，单编码，双编码，不变编码
class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s) 
        pre = 1
        if s[0] != '0':
            mid = 1
            cur = mid
        else:
            return 0
        

        for i in range(1,n):
            if s[i] == '0' and s[i-1] in {'1', '2'}:#为双编码的情况此时为 10 20两种情况
                cur = pre
                pre = mid
                mid = cur
            elif '0' < s[i-1:i+1] <= '26' and s[i-1] != '0':#此时为 [1,26]的情况，这种情况可以两个编码，也可以逐个编码
                cur = pre + mid
                pre = mid
                mid = cur
            elif (s[i-1:i+1] > '26' or s[i-1] == '0') and s[i] != '0':#s[2] > 26,并且s[i] != 0，即35，28，73等，只能依次逐个编码
                cur = mid#此时为 01，09，02等，前一个为0，后一个不为0的情况，前一个为0，01 03 09说明肯定可编码组合，
                pre = mid
            else:
                return 0
        return(cur)
            
if __name__ == "__main__":
    s = Solution()
    print(s.numDecodings("501022"))

    print(s.numDecodings("9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"))
    #3981312
"""
132. 分割回文串 II
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回符合要求的最少分割次数。

示例:

输入: "aab"
输出: 1
解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

这道题还是动态规划的问题，首先我们设定dp[ i ]表示前 i 个字符需要分几次。
有两个for 循环，第一个for是以第 i 个为结尾的字符串最少分几次。第二个 for是对第 i 个字符串前面的回文长度和个数进行判断。

动态规划的转移方程如下：

             if not temp  == temp[::-1]:
                dp[i] = min(dp[i], dp[i-1] + 1)
            else:
                dp[i] = min(dp[i], dp[j-1] + 1)


在s[ j-1 : i ]不是回文的时候， dp[i] = min(dp[i], dp[i-1] + 1)，因为不是回文，
所以这里需要分一次，前i个的总的分割次数等于前 i-1个分割次数加一。

在s[ j-1 : i ]是回文的时候，此时的前 i 个的分割次数等于前（i - 回文长度 ）+ 1 的分割次数，
由于在从后向前找回文长度的时候可能会出现多次回文，所以在计算dp[ i ]的时候取最小的一个。

但是上述方程都是取min, 初始值我们应该怎么设置? 假定初始值就是最大的需要分割的次数，
于是我使用 dp = [ i for i in range(-1,n)] 设定初始值，注意 这里的dp长度是比s的长度大一的。
————————————————
版权声明：本文为CSDN博主「Qin酱」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_38650028/article/details/107298031


"""
from typing import List
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [ i for i in range(-1,n)]
            
        for i in range(1, n+1):
            for j in range(i,0,-1):#判断回文
                temp = s[j-1:i]
                if not temp  == temp[::-1]:#不是回文，再上一个基础上加一
                    dp[i] = min(dp[i], dp[i-1] + 1)
                else:#是回文，那么等于 i减去回文长度的dp值加一
                    dp[i] = min(dp[i], dp[j-1] + 1)
        return dp[-1]
                


if __name__ == "__main__":
    s = Solution()
    print(s.minCut("abbacac"))
    # s = "abbacac"

    # print(s[2:5])
    # print(s[2:5].__reversed__())


    

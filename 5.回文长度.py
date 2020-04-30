"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

"""
#中心扩散（1）
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_l = 0
        res = ""
        for i in range(0, len(s)):
            #以s[i] 为中心向左右扩散
            left, right = i, i
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                if max_l < right - left + 1:
                    max_l = right - left + 1
                    res = s[left:right + 1]#列表左开右闭，所以右边需要加1
                left -= 1
                right += 1
                        
            #以s[i],s[i+1]为中心向左右扩散
            left, right = i, i + 1
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                if max_l < right - left + 1:
                    max_l = right - left + 1
                    res = s[left:right + 1]
                left -= 1
                right += 1            
        return res


#中心扩散（2）
def force(self, s: str) -> str:
        
        if s==s[::-1]:
            return s
        max_len = 1
        res = s[0]
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if j - i + 1 > max_len and s[i:j+1] == s[i:j+1][::-1]:
                    max_len = j - i + 1
                    res = s[i:j + 1]
        return res
        
if __name__ == "__main__":
    s = "babad"
    solution = Solution()
    output = solution.longestPalindrome(s) 
    # test = '#'+'#'.join(s)+'#' #将字符串以‘#’首尾连接
    print(output)


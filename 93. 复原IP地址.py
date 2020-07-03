"""
93. 复原IP地址
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。

 

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

"""
from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        out = []
        length = len(s)
        if length <4 or length > 12:
            return out

        def backtarck(count, ip_address,res):
            if count == 4:#有四个段之后可以进行判断
                if len(res) == 0:
                    out.append(ip_address[:-1])
                    count = 0
                return 
            #在判断数据是否合格的时候，注意 0可以加入，但是 0xx不能加入，将要加入的长度不能大于剩余长度
            for right in range(1,4):#m每次回溯的时候，下一段的长度1，2，3
                if right <= len(res) and int(res[:right]) <= 255 and (len(res[:right]) == 1 or res[0] != '0'):
                    backtarck(count+1,ip_address+res[:right]+'.',res[right:])
        backtarck(0,"",s)
        return out


if __name__ == "__main__":
    s = Solution()
    print(s.restoreIpAddresses("0100"))



    

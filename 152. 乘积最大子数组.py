"""
152. 乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

 

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。


这道题的难点在于负数会让一段乘积在正负当中变化，不好比较大小。
退一步思考，我们第 i个数是正数，那么希望前面的乘积段为正，越大越好。如果第 i 个数为负数，
那么我们希望前一段的乘积为负数，越小越好。还有一种情况就是取自身。状态转移方程如下：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200713121955686.png#pic_center)
使用两个数组，一个保存当前位次前的最大值，一个保留最小值。每次取值的时候就和之前的最大最小值相乘，
再分别赋值给最大最小数组。这样就可以减少判断正负号来回变换干扰的问题。
"""
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp_max = [i for i in nums]
        dp_min = [i for i in nums]
        for i in range(1, n):
            dp_max[i] = max(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])
            dp_min[i] = min(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])
        return max(dp_max)

if __name__ == "__main__":
  s = Solution()
  nums = [-2,3,-1]    
  nums = [-2,3,-4,-5,-1]
  print(s.maxProduct(nums))



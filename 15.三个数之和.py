from typing import List
class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort() #排序
        res = []
        for k in range(0,len(nums)-2):

            if nums[k] > 0: #最小值大于0  排除
                break
            
            if k > 0 and nums[k] == nums[k-1]:
                continue    #有两个相同的值  延后
            
            i = k + 1
            j = len(nums) -1  
            while i < j: #双指针进行比较
                s =  nums[k] + nums[i] + nums[j]
                
                if s > 0:
                    j = j - 1
                    while(i < j and nums[j+1] == nums[j]):
                        j = j - 1
                elif s < 0:
                    i = i + 1
                    while(i < j and nums[i] == nums[i-1]):
                        i = i + 1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    i += 1
                    j -= 1
                    while(i < j and nums[i] == nums[i-1]):
                        i = i + 1        
                    while(i < j and nums[j+1] == nums[j]):
                        j = j - 1                
        return res
                
                    

def main():
    s = Solution()
    l = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
    res = s.threeSum(l)
    print(res)
    #res = s.threeSum([-1,1,0,2,-1,-4,])
main()

#*************************
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        res = []
        nums = sorted(nums)#排序
        
        for i in range(len(nums)-2):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i - 1]: continue#有重复的数字，跳过
            left, right = i+1, len(nums)-1
            while left < right:#双指针运行条件
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum == 0:#符合要求，由于有去重操作，所以可以直接加入列表
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1#在双指针循环的时候，指针移动前后数值相等，就在移动一次
                    while left < right and nums[left] == nums[left-1]: left += 1
                    while left < right and nums[right] == nums[right+1]: right -= 1    
                elif three_sum < 0:
                    left += 1
                    while left < right and nums[left] == nums[left-1]: left += 1
                else:
                    right -=1
                    while left < right and nums[right] == nums[right+1]: right -= 1
        return res
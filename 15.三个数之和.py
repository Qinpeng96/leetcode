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
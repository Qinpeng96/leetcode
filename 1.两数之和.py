"""
给定一个整数数组 nums 和一个目标值 target，
请你在该数组中找出和为目标值的那两个整数，
并返回他们的数组下标。
"""
def solution(nums, target):
    if len(nums) <= 2:
        return
    for i in range(0, len(nums) - 1):
        for j in range(i+1, len(nums)):
            if(nums[i] + nums[j] == target):
                return [i, j]
"""
参考了大神们的解法，通过哈希来求解，这里通过字典来模拟哈希查询的过程。
个人理解这种办法相较于方法一其实就是字典记录了 num1 和 num2 的值和位置，而省了再查找 num2 索引的步骤。
"""

#哈希字典的赋值 hashmap[map] = index
#通过以空间换取速度的方式
def twoSum(nums, target):
    hashmap={}
    for ind,num in enumerate(nums):
        hashmap[num] = ind
    for i,num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i!=j:
            return [i,j]

            
a = [1, 3, 5, 6, 9]
b = 10
c = solution(a, b)

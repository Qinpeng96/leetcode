"给定一个整数数组 nums 和一个目标值 target，
"请你在该数组中找出和为目标值的那两个整数，
"并返回他们的数组下标。
"
def solution(nums, target):
    if len(nums) <= 2:
        return
    for i in range(0, len(nums) - 1):
        for j in range(i+1, len(nums)):
            if(nums[i] + nums[j] == target):
                return [i, j]

            
a = [1, 3, 5, 6, 9]
b = 10
c = solution(a, b)

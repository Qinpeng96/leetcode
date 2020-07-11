"""
315. 计算右侧小于当前元素的个数
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质：
 counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

示例:

输入: [5,2,6,1]
输出: [2,1,1,0] 
解释:
5 的右侧有 2 个更小的元素 (2 和 1).
2 的右侧仅有 1 个更小的元素 (1).
6 的右侧有 1 个更小的元素 (1).
1 的右侧有 0 个更小的元素.

"""

from typing import List
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
      if not nums: return []#计算为空的情况，直接返回
      nums.reverse()#翻转原始列表
      n = len(nums)
      res = [0] #因为最后一个数字比它小的肯定是 0 个
      count = [nums[0]]#将第一个数字写入计数的列表
      for key in range(1, n):#计算每一个字符比它小的数字个数，使用二分查找
        start = 0
        end = key-1
        #while循环内二分查找出当前数字应该排的位置
        while start <= end:
          mid = (start + end) // 2
          if nums[key] > count[mid]:
            start = mid + 1
          else:
            end = mid - 1
        #找出当前数字应该排的位置后插入进排序列表
        count.insert(start, nums[key])
        res.append(start)#写入当前数字的比它小的值
        # print(res)
      res.reverse()
      return res




if __name__ == "__main__":
  s = Solution()
  print(s.countSmaller([5,2,6,1]))



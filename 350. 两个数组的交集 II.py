"""
350. 两个数组的交集 II
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。
进阶:

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？



本题使用字典的思想，将两个列表转变成字典的形式，字典的key就是列表中的值，value就是每一个字符出现的次数。

首先，将两个列表建立字典，循环一个字典中的key, 通过这个key找出两个字典中key值对应的value。
选择一个最小的value次数，乘以key值，接上输出。

"""

from typing import List
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
      dict1 = Counter(nums1)
      dict2 = Counter(nums2)
      len_1 = len(nums1)
      pattern = []
      for item in dict1:#对字典1中的每个key值进行循环
        if dict2[item] != 0:#如果在字典2中存在
          for i in range(min(dict1[item], dict2[item])):#找出他们中的最小次数
            pattern.append(item)#循环加入到输出中
      return pattern


if __name__ == "__main__":
  s = Solution()
  nums1 = [4,9,9,9,5,4,5]
  nums2 = [9,4,9,8,4]
  print(s.intersect(nums1, nums2))



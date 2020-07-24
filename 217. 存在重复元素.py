"""
### 哈希集
##### 1. initialize the hash set
hashset = set() 
##### 2. add a new key
hashset.add(3)
hashset.add(2)
hashset.add(1)
##### 3. remove a key
hashset.remove(2)
##### 4. check if the key is in the hash set
if (2 not in hashset):
    print("Key 2 is not in the hash set.")
##### 5. get the size of the hash set
print("Size of hashset is:", len(hashset)) 
##### 6. iterate the hash set
for x in hashset:
    print(x, end=" ")
print("are in the hash set.")
##### 7. clear the hash set
hashset.clear()                         
print("Size of hashset:", len(hashset))
***
[217. 存在重复元素](https://leetcode-cn.com/problems/contains-duplicate/)
给定一个整数数组，判断是否存在重复元素。

如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true
***
使用哈希表进行记录，
"""
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return True
            else:
                dic[nums[i]] = 1
        return False

```

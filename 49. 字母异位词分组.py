"""
[49. 字母异位词分组](https://leetcode-cn.com/problems/group-anagrams/)
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。
***
开始我想的是使用Counter计数来分类，但是这个可以考虑使用他们的排序后的值加上字典进行记录。
每次从strs中拿一个字符串出来，进行排序，注意排序sorted后的是一个字符组，还需将这个字符串连接在一起作为一个字符串。

将排序后的字符串作为字典的key, 如果之后的字符串排序后与key相等，那么就将这个值连接到这个key的键值后面，也就是所谓的一个key,对应于多个键值。

"""
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs: return []
        res = {}

        for item in strs:
            sorted_item = '' .join(sorted(item))
            if sorted_item not in res:
                res.setdefault(sorted_item,[]).append(item)
            else:
                res.setdefault(sorted_item,[]).append(item)
        return list(res.values())
        
#这是一种更加简洁的写法
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
	    dic = {}
        for s in strs:
            keys = "".join(sorted(s))
            if keys not in dic:
                dic[keys] = [s]
            else:
                dic[keys].append(s)
        return list(dic.values())


"""
[4. 寻找两个有序数组的中位数](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
"""
```python
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int])->float:
        nums1 = nums1 + nums2
        nums1.sort()
        i = (len(nums1)-1) // 2 #由于中位数有的是要计算左右两数的平均值
        j = len(nums1) // 2 #所以当列表的个数为偶数的时候，需要进行平均值计算
        value = (nums1[i] + nums1[j]) / 2
        return value

if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    solution = Solution()
    output = solution.findMedianSortedArrays(nums1, nums2)
    print(output)
```
"""
显然上述的解法是O((m+n) log (m+n))的，不满足题意，看到log应该考虑使用二分查找。
看看威威哥的题解之后在这里记录一下。

由于两个数组是有序的，那么我们找出来的中位数的次序是固定的，我们可以通过从头开始比较两个数组元数进行计数，找到中位数。但是这样的时间复杂度是O(m+n),也是不满足题意的。

承接上面的思路，我们可以在两个数组中各自划分一条线，把数组变成左右两边。只要两个数组的左边个数等于右边的个数和。或者两个数组的左边个数和 等于 右边个数和加一，那么我们就可以求的中位数了。

还是一步一步分析，首先看看两个数组个数和为奇数的情况

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200814094731345.png#pic_center)
如上图所示，为奇数个数的时候，分割线左边的个数和始终要大于右边的个数和加一个。我们的中位数就在两个分割线左边值里面去一个最大数。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200814094643375.png#pic_center)
如果两个数组之和是偶数，那么根据上面的分割关系，左右两边的个数相等，中位数就是中间的两个数取平均值。但是由于分割线左右两边有四个元素，我们应该取左边的最大值， 右边的最小值计算平均。
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020081410060035.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)

使用二分法：
- 首先看二分的具体弹出条件是什么？无论是奇数个还是偶数个总数，对于分割线的左右数值：
	- 第一个数组左边的值，肯定要小于第二个数组右边的值
	- 第一个数组右边的值要大于第二个数组左边的值
	- 如果第一个数组右边的值小于第二个数组左边的值，那么那么说明一个数组的分割线靠左了，应该右移。
	- 反之，如果第一个数组的左边的值大于第二个数组的右边的值，说明该分割线取得靠右了，需要左移。
- 边界的取值：知道使用二分之后，我们来确定一下边界：
	- 	首先是哪一个数组在前的问题，这里使用长度较短的数组在第一个每减少在第一个数组中二分的时间
	- 在第一个数组中进行二分的时候， 我们可以通过（left + right )// 2取得中间的分割线，第二个数组的分割线由于我们知道中位数所在得长度，所以我们取得是两个数组长度和减去第一个数组中得中位线，即（n1+n2+1）- mid。这里加一的原因是我们需要左边的数组等于右边的数组和，或者左边的数组和等于右边的数组和加一，所以这里有一个加一。
	- 在left == right的时候就弹出，这个时候如下图所示，有四种边界情况需要讨论

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200814100654628.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)				

- 在弹出的时候由于left等于right， 可能就是left == 0, 或者 left = n1的情况。
	- 当left等于0的时候，我们取值取得是nums[left-1]，所以数组就会越界，这里将这种情况赋值为负无穷，任意一个值在取max的时候都比他他。
	- 当left 的值为n1的时候，我们取nums[left]也会越界，所以这里去一个正无穷，任意值和其取最小值，都是本身。


实现的代码如下：
"""
```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int])->float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1
        left, right = 0, n1

        while left < right:#进行二分查找
            i = (left + right) // 2
            j = (n1 + n2 + 1)//2 - i#这里多加一个1，意味着左边个数等于，或者比右边个数多个1
            if nums1[i] < nums2[j-1]:
                left = i + 1
            else:
                right = i
        i = left
        j = (n1 + n2 +1) // 2 -i
        #左边越界的时候取负无穷
        m1 = nums1[i-1] if i > 0 else -float('inf')
        m2 = nums2[j-1] if j > 0 else -float('inf')
        if (n1+n2) % 2 == 1:
            return max(m1, m2)#为奇数个的时候， 取左边界的最大值
        #右边越界的时候取正无穷
        m3 = nums1[i] if i < n1 else float('inf')
        m4 = nums2[j] if j < n2 else float('inf')
        if (n1+n2) % 2 == 0:#为偶数个的时候，取左边界的最大值，右边界的最小值，两者求一个平均
            return (max(m1, m2)+min(m3,m4)) / 2
```

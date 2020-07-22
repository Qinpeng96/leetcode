"""
[剑指 Offer 11. 旋转数组的最小数字](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/)
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
***
这道题主要是想考察二分法，但是这里的二分法和之前的又有一些不一样。下面的分析来之力扣大佬的解析：

循环二分： 设置 i, j 指针分别指向 numbers 数组左右两端，m = (i + j) // 2为每次二分的中点（ "//" 代表向下取整除法，因此恒有 i≤m<j ），可分为以下三种情况：

 1. 当 numbers[m] > numbers[j]时： m 一定在 左排序数组 中，即旋转点 x 一定在 [m + 1, j]闭区间内，因此执行 i = m + 1；
 2. 当 numbers[m] < numbers[j] 时： m 一定在 右排序数组 中，即旋转点 x 一定在[i, m]闭区间内，因此执行 j = m；
 3. 当 numbers[m] == numbers[j] 时： 无法判断 m 在哪个排序数组中，即无法判断旋转点 x 在 [i, m]还是 [m + 1, j] 区间中。解决方案： 执行 j = j - 1缩小判断范围 （分析见以下内容） 。

**注意**：
无法判定 mm 在左（右）排序数组： 设以下两个旋转点值为 00 的示例数组，则当 i = 0i=0, j = 4j=4 时 m = 2m=2 ，两示例结果不同。

例 [1, 0, 1, 1, 1] ：旋转点 x = 1 ，因此 m = 2 ，在 右排序数组 中。
例 [1, 1, 1, 0, 1]：旋转点 x = 3，因此 m = 2，在 左排序数组 中。

这里对 right 减一就相当于是缩小边界，每次都缩小一位，直到将右边的重复数字排除。

作者：jyd
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solution/mian-shi-ti-11-xuan-zhuan-shu-zu-de-zui-xiao-shu-3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if not numbers: return 
        left, right = 0 , len(numbers)-1
        while left < right:#二分查找,分为三种情况，中>右，中<右，中==右
            mid = (left + right) // 2
            # print(left, mid,right)
            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] < numbers[right]:
                right = mid
            else:#两者相等不能判断最小值是在左还是在右
                right -= 1
        return numbers[left]


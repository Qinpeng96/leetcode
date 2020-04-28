"""

实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1


*********************************************************

算法推导
如何得到这样的排列顺序？这是本文的重点。我们可以这样来分析：

1.我们希望下一个数比当前数大，这样才满足“下一个排列”的定义。因此只需要将后面的「大数」与前面的「小数」交换，
就能得到一个更大的数。比如 123456，将 5 和 6 交换就能得到一个更大的数 123465。
2.我们还希望下一个数增加的幅度尽可能的小，这样才满足“下一个排列与当前排列紧邻“的要求。
为了满足这个要求，我们需要：
    1)在尽可能靠右的低位进行交换，需要从后向前查找
    2)将一个 尽可能小的「大数」 与前面的「小数」交换。比如 123465，下一个排列应该把 5 和 4 交换而不是把 6 和 4 交换
    3)将「大数」换到前面后，需要将「大数」后面的所有数重置为升序，升序排列就是最小的排列。以 123465 为例：
    首先按照上一步，交换 5 和 4，得到 123564；然后需要将 5 之后的数重置为升序，得到 123546。显然 123546 比 123564 更小，
    123546 就是 123465 的下一个排列
以上就是求“下一个排列”的分析过程。

算法过程
标准的“下一个排列”算法可以描述为：

1.从后向前查找第一个相邻升序的元素对 (i,j)，满足 A[i] < A[j]。此时 [j,end) 必然是降序
2.在 [j,end) 从后向前查找第一个满足 A[i] < A[k] 的 k。A[i]、A[k] 分别就是上文所说的「小数」、「大数」
3.将 A[i] 与 A[k] 交换
4.可以断定这时 [j,end) 必然是降序，逆置 [j,end)，使其升序
5.如果在步骤 1 找不到符合的相邻元素对，说明当前 [begin,end) 为一个降序顺序，则直接跳到步骤 4




\\\\————————————————/////
举个例子：nums[1 2 3 8 5 7 6 4]
1 2 3 8 5 7 6 4：从右向前 第一个降序位置5-7,即相邻升序为(i,j)=(4,5)      ||||———>||||
1 2 3 8 5 7 6 4:在(j:end)之后从右到左查找比nums[i]大的数nums[k],第k=6个    ||||<———||||
1 2 3 8 6 7 5 4:交换nums[i]与nums[k]                                     |||<---->|||
1 2 3 8 6 4 5 7：对nums[j:end]之后翻转
/////————————————————\\\\

*********************************************************
作者：imageslr
链接：https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-suan-fa-xiang-jie-si-lu-tui-dao-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)#获得列表的长度
        #如果列表为空或者1个，则返回原值
        if nums_len == 0 or  nums_len == 1: 
            return nums
        #从右向左查找到第一个升序的位置
        left = nums_len - 1
        while left > 0 and nums[left] <= nums[left - 1]:#注意有等号
            left -= 1   
        #如果整个列表都是降序，则翻转整个列表
        if left == 0: nums.reverse()
        else:
            right = nums_len - 1
            #从右向左找一个比升序首地址大的数，letf - 1 为从右到左第一个升序的首地址
            while left - 1 < right and nums[left - 1] >= nums[right]:
                right -= 1
            #找到之后对两者进行交换
            temp = nums[right]
            nums[right] = nums[left - 1]
            nums[left - 1] = temp
            #对交换完升序首地址之后的列表[left:end]进行翻转
            for i in range((nums_len - left)//2):
                i = i + left
                temp = nums[i]
                nums[i] = nums[nums_len - i + left - 1]
                nums[nums_len - i + left - 1] = temp
        return nums

if __name__ == "__main__":
    input_num = [1,2,3,8,5,7,6,4]
    input_num = [5,2,2]
    solution = Solution()
    output = solution.nextPermutation(input_num)
    print(output)
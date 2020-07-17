 """
703. 数据流中的第K大元素
设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。

你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。

示例:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
说明:
你可以假设 nums 的长度≥ k-1 且k ≥ 1。
"""
"""
由于在看二叉搜索树的教程，里面要求使用二叉树来做这个题目，所以第一种方法就是通过构建二叉搜索树来完成的。

首先建立TreeNode的类，多一个count属性, 计算它包含的节点的数量
之后创建一个查找第K大的元素的函数方法，findKHelper，返回节点； 创建一个插入元数到二叉搜索树的方法，
这里使用的是insertIntoBST，在插入元素的左右判断大小的过程中，还需要对其计数count进行增加。
开始初始化，初始化的工作就是将数组 nums创建为一个二叉搜索树，。如果之前二叉搜索树内的节点数已经有 K个，
现在还需要加入，就需要使用上述的查找函数，找到第K大的数的值和待插入的数的值作比较。

如果待插入的值大于第K 大的值，才需要插入操作，并且更新第K大的值。
add函数就是将一个新的值插入，找出第k大，我们这里需要注意的是，只有当待插入的值大于第K大的值，
或者第K大的值不存在的时候我们才需要插入操作，否则直接计算第K大的值返回就可以了。
————————————————
版权声明：本文为CSDN博主「Qin酱」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_38650028/article/details/107402694
"""
####################################

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.count = 1

class KthLargest:
    def insertIntoBST(self, cur: TreeNode, val: int) -> TreeNode:#新元素插入到二叉搜索树中
        if not cur: #节点为空，第一次添加或者是 递归过程中找到需要接入的位置
            cur = TreeNode(val)
            return cur
        if val > cur.val:#查找到需要添加的位置，递归，在上一步，为空的时候进行返回，接到左右节点上
            cur.right = self.insertIntoBST(cur.right, val)
        else:
            cur.left = self.insertIntoBST(cur.left, val)
        cur.count += 1# 每一个节点的包含点计数器加一
        return cur

    def __init__(self, k: int, nums: List[int]):#初始化二叉搜索树
        self.k = k #第 k 大
        self.root = None #根节点
        self.klarge = None #第k大的数值

        for num in nums:#创建搜索二叉树
            if not self.root or self.root.count < k:#如果根节点为空，或者二叉树内的节点个数小于 k,插入
                self.root = self.insertIntoBST(self.root, num)
            #由于二叉搜索树内现在最多保存 k个值，所以如果有新数加入，就会有老数删除
            else:
                if not self.klarge:#如果没有第k大数的值，就计算第 k 大的值
                    self.klarge = self.findKHelper(self.root, self.k).val
                if num > self.klarge:#如果当前的值大于第 k 大的数，需要插入，重新找到第K大的数
                    self.root = self.insertIntoBST(self.root, num)
                    self.klarge = self.findKHelper(self.root, self.k).val


    def findKHelper(self,cur:TreeNode,k)->TreeNode:#查找当前二叉搜索树内第K大的元素
        #查找第K大元素，首先根节点有所有节点的个数值，右子节点有右边的节点个数，这样
        #我们就看可以通过右子节点的个数确定出根节点的值是第几大，如果没有右子节点，那么根节点就是最大
        order = 1#由于节点的计数器包含自身，所以这里需要补充一个 1。默认根节点第一大
        if cur.right:#如果根节点还有右子节点，那么最大次序发生变化
            order += cur.right.count
        #接下来我们知道了根节点为第order大之后，需要判断  k 与 order 之间的关系
        if order == k:#刚好找到
            return cur
        elif order > k:
            return self.findKHelper(cur.right, k)
        else:
            return self.findKHelper(cur.left, k - order)# 因为左子树都比 order小，在order的基础上再找

    def add(self, val: int) -> int:
        #self.kLarge没有值，或者当前值大于self.kLarge才插入
        if self.klarge and val > self.klarge or not self.klarge:
            self.root = self.insertIntoBST(self.root, val)
        self.klarge = self.findKHelper(self.root, self.k).val#插入之后重新查找新的第K大的值
        return self.klarge



#############################################################################
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.count = 1

class KthLargest:
    def insertIntoBST(self, cur: TreeNode, val: int) -> TreeNode:
        if not cur:#首次插入元素
            cur=TreeNode(val)
            return cur
        if cur.val<val:#插入元素比当前元素大，插入至右子树
            cur.right=self.insertIntoBST(cur.right,val)  
        else:#插入元素比当前元素小或等于，插入至左子树
            cur.left=self.insertIntoBST(cur.left,val)
        cur.count+=1#若插入至子树，当前节点的count需要+1
        return cur 
    def __init__(self, k: int, nums: List[int]):
        self.root=None 
        self.k=k
        self.kLarge=None#记录第k大
        for i in nums: 
            #若根节点为空，或者根节点的count<k直接插入
            if not self.root or self.root.count<k :
                self.root=self.insertIntoBST(self.root,i)  
            else:#当前二叉搜索树的元素数>=k
                if not self.kLarge:#计算第k大
                    self.kLarge=self.findKHelper(self.root,k).val
                if i>self.kLarge:#如果当前值大于第k大，插入并重新寻找第k大
                    self.root=self.insertIntoBST(self.root,i) 
                    self.kLarge=self.findKHelper(self.root,k).val

    def findKHelper(self,cur:TreeNode,k)->TreeNode:
        curCnt=1#如果无右节点，当前是第1大的数
        if cur.right:#如果有右节点，则当前是cur.right.count+1大的数
            curCnt+=cur.right.count
        if k==curCnt:#当前值即为第k大
            return cur
        elif k<curCnt:#第k大在右子树
            return self.findKHelper(cur.right,k)
        else:#第k大在左子树，为左子树的第k-curCnt大
            return self.findKHelper(cur.left,k-curCnt)

    def add(self, val: int) -> int:
        #self.kLarge没有值，或者当前值大于self.kLarge才插入
        if self.kLarge and val>self.kLarge or not self.kLarge:
            self.root=self.insertIntoBST(self.root,val)
        self.kLarge=self.findKHelper(self.root,self.k).val
        return self.kLarge

作者：miraachan
链接：https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/solution/python3er-cha-sou-suo-shu-shu-ju-liu-zhong-de-di-k/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

############################################################################
from heapq import *


class KthLargest(object):
    
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        heapify(self.nums)
        while len(self.nums)>self.k: #cut heap to size:k
            heappop(self.nums)
        
    
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) < self.k:s
            heappush(self.nums, val)
            heapify(self.nums) #cation
        else:
            top = float('-inf')
            if len(self.nums) > 0:
                top = self.nums[0]
            if top < val:
                heapreplace(self.nums, val)
        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

作者：plusone-z
链接：https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/solution/703-pythonshi-xian-shu-ju-liu-zhong-di-kda-xiao-di/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
[剑指 Offer 33. 二叉搜索树的后序遍历序列](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/)
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。


参考以下这颗二叉搜索树：
#
	     5
	    / \
	   2   6
	  / \
	 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true
***
我开始也是用的递归，因为列表的最后一个值就是根节点的值，我们可以通过比较，将左子树和右子树区分出来，并且左子树列表的左后一个值就是其左子树的根节点，右子树列表的最后一个值就是其右子树的根节点。

我是一开始找到最后一位，即整个树的根节点。但是在判断子树是否合法的时候没有想到怎么判断子树是否合法。
我是知道找左右子树的根节点，然后一分为二， recur(i, m-1), recur(m, j-1)但是就是没有对前面的有效性进行判断。



![在这里插入图片描述](https://img-blog.csdnimg.cn/2020081113561945.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
从上图可以发现，一个子树的根节点根据二叉搜索树的性质，是大于其左子树，小于其右子树的。所以可以对数值进行从左到右的遍历。前半段找一个值大于根节点，即最后一个数，那么这个数的就是右子树区间的开始。注意，我们还要判断右子树是否合法，继续遍历，当指针的数值大于最后的根节点时继续增加。最后通过 指针索引 p 和 最后一个值的索引 j 是否相等来判断是否合法。

这里可能会有疑问，加入前半段的值都是小于最后的根节点，但是其中有部分值不对，不是一个二叉搜索树。我们在第一遍得时候，只关心本次得节点分割点，和前后半段得总体数值是否满足条件，具体得每一个小子树是否满足二叉搜索树，是需要在之后得递归中进行一不进行判断得。
"""
```python
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recur(i, j):
            if i >= j: return True#只有一个值的时候，或者已经判断完了
            p = i
            root = postorder[j]
            while postorder[p] < root:#判断前半段值，找到右子树得起始节点
                p += 1
            m = p
            while postorder[p] > root:#判断后半段的值，并且弹出的时候对p和j 进行判断，看是否合法
                p += 1
            return p == j and recur(i, m-1) and recur(m,j-1)        
        return recur(0, len(postorder)-1)

```
大佬的单调栈解法：
#
	后序遍历：   left -> right -> root
	后序的逆序： root-> right-> left
	
为什么要用单调栈呢，因为往右子树遍历的过程，value是越来越大的，一旦出现了value小于栈顶元素value的时候，就表示要开始进入左子树了（如果不是，就应该继续进入右子树，否则不满足二叉搜索树的定义，不理解的请看下二叉搜索树的定义），但是这个左子树是从哪个节点开始的呢？

单调栈帮我们记录了这些节点，只要栈顶元素还比当前节点大，就表示还是右子树，要移除，因为我们要找到这个左孩子节点直接连接的父节点，也就是找到这个子树的根，只要栈顶元素还大于当前节点，就要一直弹出，直到栈顶元素小于节点，或者栈为空。栈顶的上一个元素就是子树节点的

接下来，数组继续往前遍历，之后的左子树的每个节点，都要比子树的根要小，才能满足二叉搜索树，否则就不是二叉搜索树。

- 首先接入的根节点 stack
- 


```python
class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        stack, root = [], float("+inf")#初始化根节点为正无穷大
        for i in range(len(postorder) - 1, -1, -1):#倒序遍历列表串
            if postorder[i] > root: return False#遍历的值大于根节点，返回false
            while(stack and postorder[i] < stack[-1]):#当栈不为空，前当前值小于栈顶值得时候，弹栈，弹到左子树去
                root = stack.pop()
            stack.append(postorder[i])#这里时接左子树节点
        return True

作者：jyd
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/solution/mian-shi-ti-33-er-cha-sou-suo-shu-de-hou-xu-bian-6/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

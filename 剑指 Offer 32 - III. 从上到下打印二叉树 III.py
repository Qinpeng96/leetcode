"""
[剑指 Offer 32 - III. 从上到下打印二叉树 III](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/)
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],
#
	    3
	   / \
	  9  20
	    /  \
	   15   7
返回其层次遍历结果：
#
	[
	  [3],
	  [20,9],
	  [15,7]
	]
***
在之前的层序遍历的时候，每次我们都是先加入的左节点，后加入的右节点。如果要求是从右到左：我们每一层就先加入右节点，再加入左节点。

开始我想的是，这个不就是一次先加左节点，后加右节点； 下一次就先加右节点再加左节点么？但是这里有一个问题，请看下面的例子:
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200811111628559.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
按照之前的思路顺序是这样：
#
	[3, 20, 9, 34, 4, 15,7] 我们的第三层从左到右确实是从左到右，但是只是一个节点的从左到右，而不是整层节点的从左到右。
究其原因是我们使用的双向队列，如果我们每次使用的是栈，那么上一层后加入的元数这一层就会先弹出，就满足了Z字型遍历的条件。
所以这里使用了一个临时的temp 栈存贮下一层的节点顺序，这里不能直接加入queue中，因为这里的queue不是双向队列，而是一个后进先出的栈。
如果我们遍历的时候就加入栈内，就会在下一次被弹出。所以这里只能设置一个临时的保存栈，在当前层遍历完了之后在赋值给queue。
"""
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        queue, out = [], []
        queue.append(root)
        cnt = -1

        while queue:
            n = len(queue)
            res = []#每一层的节点值输出
            temp = []#临时保存下一层节点的栈
            cnt += 1
            for _ in range(n):
                node = queue.pop()
                res.append(node.val)
                if cnt & 1:#先右后左
                    if node.right: temp.append(node.right)
                    if node.left: temp.append(node.left)
                else:#先左后右       
                    if node.left: temp.append(node.left)
                    if node.right: temp.append(node.right)
            queue = temp              
            out.append(res)
        return out
```
接下来还是看看大佬的代码把：

层序遍历 + 倒序
此方法的优点是只用列表即可，无需其他数据结构。
偶数层倒序： 若 res 的长度为 奇数 ，说明当前是偶数层，则对 tmp 执行 倒序 操作。

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp[::-1] if len(res) % 2 else tmp)
        return res

作者：jyd
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/solution/mian-shi-ti-32-iii-cong-shang-dao-xia-da-yin-er--3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

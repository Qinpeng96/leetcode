"""
[剑指 Offer 36. 二叉搜索树与双向链表](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/)
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

 

为了让您更好地理解问题，以下面的二叉搜索树为例：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200811182210541.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200811182244280.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center) 特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。
***
这道题也是一开始没有一点点思绪=-=。看了下K神大佬的文字分析，之后还是弄出来了。
主要是双向链表连接需要一个头节点，根据大佬的思路，建立一个全局的链头self.head， 一个前驱节点self.pre，这样一来在每次中序遍历的时候，使用前驱节点去连接当前的节点。

最后遍历完了之后再将链表的头尾连接起来。
K神的解析链接再[这里](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/solution/mian-shi-ti-36-er-cha-sou-suo-shu-yu-shuang-xian-5/), 下面是K神的图片：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200811182642552.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)

"""
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':


        def solve(root):
            if not root: return 
			#使用的是中序遍历
            solve(root.left)
            if self.pre:#如果前驱节点存在
                self.pre.right = root#将前驱和当前节点两个相互连接
                root.left = self.pre
                self.pre = root#连接完了之后，前驱节点后移
            else:#如果前驱节点不存在，意味着找到的是中序遍历的第一个节点
                self.head = root
                self.pre = root
            solve(root.right)

        if not root: return None
        self.pre = None
        self.head = None
        solve(root)
        self.head.left = self.pre#最后连接两个头尾节点
        self.pre.right = self.head
        return self.head
            
```

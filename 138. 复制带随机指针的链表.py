"""
[138. 复制带随机指针的链表](https://leetcode-cn.com/problems/copy-list-with-random-pointer/)
给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的 深拷贝。 

我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
***
这道题目和[133.克隆图](https://leetcode-cn.com/problems/clone-graph/)相似，但是克隆图那道题主要是考察一个深度优先搜索，对每一个邻居进行DFS.这道题有几个坑：
- 首先是随机指针，不知道指向那里，如果我们再指向的时候另一个节点还没有被复制，那么这样子是不对的。
- 已经知道上面的坑了，我们使用DFS先复制链表，再复制节点这下随机指针就不会跑飞了。
- 但是这里还有一个问题：随即指针可能会产生一个环，我们一直随机指针复制下去，可能会陷入死循环。所以使用一个字典来进行记录.在下面这种情况下我们打印一下字典值看一看：
#
	输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
	输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
	
![在这里插入图片描述](https://img-blog.csdnimg.cn/202008051800559.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
#
	遍历的顺序如下：7->13->11->10->1->7->11->1->7
	开始是链表遍历：7->13->11->10->1
	接着就是随机指针的遍历：1->7(重复) 10->11(重复) 11->1(重复) 13->7(重复)  7->null(弹出)
	

"""
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = {}#建立字典的作用就是防止陷入循环
        def dfs(head):
            if not head:return 
            if head in dic:
                return dic[head]
            clone = Node(head.val)
            dic[head] = clone
            clone.next = dfs(head.next)#首先复制的是链表，否则random会有时候找不到节点
            clone.random = dfs(head.random)
            return clone

        return dfs(head)
```

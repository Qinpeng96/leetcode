"""
[429. N叉树的层序遍历](https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/)
给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。

例如，给定一个 3叉树 :

 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200717143200292.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
返回其层序遍历:

[
     [1],
     [3,2,4],
     [5,6]
]
 
说明:

树的深度不会超过 1000。
树的节点总数不会超过 5000。
***
这是自己写的一个层序遍历得方法：

 1. 首先建立两个双向队列，和两个空列表。双向队列作为存储当前层的节点与下一层的节点。而两个列表中一个作为最终输出，一个作为每层的输出。
 2. 初始的时候判断一下是否为空，然后就将root第一个节点加入pre_queue队列。进入while循环：当pre_queue列表为空的时候，结束循环。
 3. pre_queue队列里面装的是当前层的节点，res里面是下一层的节点值，queue里面是下一层的节点。
 4. 循环内的主要逻辑：将当前层的节点的子节点右进装入queue,数值装入res；直到当前层没有节点，即pre_queue内为空。此时将res内保存的值加入到out输出。
 5. 因为while pre_queue是当pre_queue为空就结束，但是我们还有下一层的值没有遍历，所以在while循环的最后就把下一层的queue赋值给 pre_queue，并将queue清零。
 6. 最后还有一个特数情况，就是在最后一层的时候，当前层没有子节点，就不用进入到for循环内找当前层的子节点。这时的res是空的，所以如果当前层都没有子节点，并且已经判断遍历完了，那么可以直接返回out输出值。
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return None#对初始为空的判断
        #建立两个队列，两个列表
        queue = collections.deque()
        pre_queue = collections.deque()
        res = []
        out = []
        pre_queue.append(root)#初始加入队列和列表
        out.append([root.val])
		#进行循环遍历每一层
        while pre_queue:
            node = pre_queue.popleft()#从队列左边弹出节点，寻找其当前层的子节点，将其加入queue
            if node.children:#如果当前层的下一层有子节点，将其所有值加入res,节点加入queue
                for chl in node.children:
                    res.append(chl.val)
                    queue.append(chl)

            if not pre_queue:#当前层为空，说明本层已经遍历完
                if not res:#如果res也为空，说明没有下一层，本层即最后一层，直接返回输出
                    return out
                else:#如果res不为空，将res的值加入out,把下一层的节点赋值给本层，并清空下一层内接节点
                    out.append(res)
                    res = []
                    pre_queue = queue.copy()
                    queue.clear()

        return out

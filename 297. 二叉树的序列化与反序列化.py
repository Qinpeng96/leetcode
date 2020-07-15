"""
297. 二叉树的序列化与反序列化
https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，
同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，
你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。
你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。


1.首先我们需要对树进行编码，编码的方式有很多，前序遍历，中序遍历，后序遍历等等。这里使用的是前序遍历，因为前序遍历的初始点是根节点，
所以前序遍历比较方便。之前使用的是递归的方法对树进行前序遍历，现在由于之后需要进行解码，由字符串还原成树，使用BFS比较方便。
于是这里选用队列进行编码、解码。

2.队列的性质，python中的队列是从collections中的一个方法 collections.deque( ),创建一个双向队列。双向队列的使用方法相对于之前的
列表list有所不同，双向列表可以左右都加入、弹出元素。
##### 例如
		queue.append() 				#右加入
		queue.appendleft()			#左加入
		queue.pop() 				#右弹出
		queue.popleft() 			#左弹出



3.在把树分解加入队列的过程中我们具体分析一下其中的流程：

 - 将根节点加入队列中 [1]
 - 进行队列是否为空的循环， 从左弹出队列里面最左端的元素1，作为当前的根节点，如果该节点不为空，则为其增添左右两个节点到队列中。
    使用数字表示如下[ [2, 3] ] 
 - 在加入两个子节点后弹出最左端的节点[ [2, 3] ]-->[ [3]],此时弹出的是2，这次循环2不为空，就要为2增加它的左右子节点到队列中
    即 [ [3], [4, 5] ]。
 - 之后再弹出3，增加3的子节点到队列中。。。由此类推。
 - 我们加入输出列表的顺序就是非空的弹出顺序，弹出一个非空节点，就将其值加入列表。


4.在上述编码过程中我们得到了一个字符串，之后就是对这个字符串进行解码。

 - 首先是除去字符串的左右边界和中间的分割逗号，设定字符串的起始索引 index i = 1
 - 之后就将字符串中的首字符的值创建一个根节点，和上述的方法类似，接下来就是对字符串的解码
 - 将队列中的元数从左弹出，如果索引 1 的字符不为空，有值，则创建一个节点，作为上述的左字节，并且加入队列，
    为了之后弹出本次的节点时，为本节点找子节点。
 - 之后索引加一，如果对应字符非空，创建一个节点，作为弹出的右节点，加入队列。
 - 注意，这里由于每次增加左右子节点的时候，我们的节点是在下移的，所以一开始我们设定的root为根节点，之后弹出之后使用node 代替，
    方便最后返回的时候能够找到根节点进行返回。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root: return '[]'#原始树为空，直接返回
        queue = collections.deque()
        queue.append(root)#将根节点加入队列
        while queue:
            node = queue.popleft()#将最左边的节点弹出队列
            if node:#对节点进行判断，如果为空，则返回 null,不为空，考虑加入左右子节点
                res.append(str(node.val))#节点不为空，加入输出列表
                queue.append(node.left)#再将此节点的左右子节点加入队列，子节点的左右以null结尾
                queue.append(node.right)
            else:
                res.append('null')
        return '['+ ','.join(res) + ']'


    def deserialize(self, data):
        """Decodes your encoded data to tree.      
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]': return None
        val = data[1:-1].split(',')
        i = 1
        root = TreeNode(int(val[0]))#创立一个根节点
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()#每次弹出一个节点node，下面为其加入两个子节点
            if val[i] != 'null':
                node.left = TreeNode(int(val[i]))#添加左节点
                queue.append(node.left)#并将添加的左节点加入队列
            i += 1
            if val[i] != 'null':
                node.right = TreeNode(int(val[i]))#添加右节点
                queue.append(node.right)#并将添加的右节点加入队列
            i += 1
        return root#最后返回的时候返回的是原始建立的root根节点，因为之后都是用的node操作

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
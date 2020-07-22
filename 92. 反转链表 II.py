"""
[92. 反转链表 II](https://leetcode-cn.com/problems/reverse-linked-list-ii/)
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
*****

由于要求使用一次遍历，所以首先找到翻转开始以及开始的前一个位置，对之后的数进行（n-m）次翻转。重点在于对链表的翻转。
 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200722230228191.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)

"""
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pre = ListNode(-1)
        node = pre
        pre.next = head
        for _ in range(m-1):
            pre = pre.next#找到left的起始前的位置 

        cur = pre.next#开始转化的位置
        for _ in range(n-m):#交换多少次
            temp = cur.next#交换过程看上面的图片
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp
       
        return node.next                
```

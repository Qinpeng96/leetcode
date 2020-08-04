"""
[160. 相交链表](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/)
编写一个程序，找到两个单链表相交的起始节点。

如下面的两个链表：

![在这里插入图片描述](https://img-blog.csdnimg.cn/2020080414401121.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)

在节点 c1 开始相交。



示例 1：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200804144006159.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)


输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
***
这道题的思路有点像有环链表去找一个环的入口一样。
两个链表同时开始往后移，当一个链表移动到尾部时候，就换到另一个链表的表头开始移动。这样两者都会走一样长的路程，最后在输出相同的其实节点即可。

"""

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headB or not headA: return None
        piontA, piontB = headA, headB
        cnt = 0

        while piontB != piontA:
            piontB = piontB.next
            piontA = piontA.next
            if not piontA: #找到当前的链表尾部，换到另一个链表的表头
                piontA = headB
                cnt += 1

            if not piontB: #找到当前的链表尾部，换到另一个链表的表头
 				piontB = headA
                cnt += 1
                
            if cnt > 2:#只需要对接两次就可以了，如果两次之后还是没有相遇，那么肯定不会相遇
                return None
        return piontA
```
"""
其实我这里考虑交换链表无线循环是没有必要的，因为链表的尾部都是接的None,那么肯定有一个None是相等的。
"""
```python
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha

作者：jyd
链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/intersection-of-two-linked-lists-shuang-zhi-zhen-l/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

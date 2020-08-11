"""
[剑指 Offer 31. 栈的压入、弹出序列](https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/)
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

示例 1：

输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
示例 2：

输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
输出：false
解释：1 不能在 2 之前弹出。
 

提示：

0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed 是 popped 的排列。
***
思路就是完全模拟栈的进入弹出，每次待加入的时候，栈顶元数与出栈元数对比，如果相等，则出栈，出栈元数索引加一。否则就进栈，进栈元数索引加一。

注意：在while循环内的入栈索引是可以等于n的，这是因为我们i == n，这个时候入栈的最后一个元素才能加入进去，加入进去之后还需要做比较，
所以这个时候不能终止循环。但是我们在循环内部加入stack的时候，i的索引是小于n的，因为之后这样待加入的元数索引才满足条件。
"""
```python
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        stack = []
        j = 0
        i = 0
        while  0<= i <= n and j < n:
            if not stack and i < n: #栈为空的时候入栈
                stack.append(pushed[i])
                i += 1
            elif  i < n and stack[-1] != popped[j]:#之前的栈顶和弹栈元数不相同，本次可以入栈
                stack.append(pushed[i])
                i += 1
            elif stack[-1] == popped[j]:#之前元素和弹栈元数相同，弹栈，弹栈索引加一
                stack.pop()
                j += 1
            else:#否则就是一些不匹配的情况，直接返回False
                return False
        return True if not stack else False#最后栈内为空则返回True
```
大佬终究是大佬：

```python
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [], 0
        for num in pushed:
            stack.append(num)#每次加入元数入栈
            while stack and stack[-1] == popped[i]:#循环判断出栈
                stack.pop()
                i += 1#出栈后弹栈的索引加一
        return not stack

作者：jyd
链接：https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/solution/mian-shi-ti-31-zhan-de-ya-ru-dan-chu-xu-lie-mo-n-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

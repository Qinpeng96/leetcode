"""
[946. 验证栈序列](https://leetcode-cn.com/problems/validate-stack-sequences/)
给定 pushed 和 popped 两个序列，每个序列中的 值都不重复，只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，返回 true；否则，返回 false 。

示例 1：
输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 
***
- 每次循环我们都push数字入栈。对比当前待出栈的元数是否在栈顶，如果不在，就继续循环入栈。
- 如果当前栈顶的元素和待出栈的元素相同，那么进行pop出栈，弹栈之后popped序列的索引后移，继续看此时待出栈的元素和栈顶元素是否相同。

"""

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
```

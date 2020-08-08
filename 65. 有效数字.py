"""
[65. 有效数字](https://leetcode-cn.com/problems/valid-number/)
验证给定的字符串是否可以解释为十进制数字。

例如:

"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。这里给出一份可能存在于有效十进制数字中的字符列表：

数字 0-9
指数 - "e"
正/负号 - "+"/"-"
小数点 - "."
当然，在输入中，这些字符的上下文也很重要。
***
下面的推导来自力扣的题解
主要是由四种输入：小数点，正负号，数字，指数e 。根据这一点我们可以推导出一些结论：

- 空格只能出现在首尾，出现在中间一定是非法的。
- 正负号只能出现在两个地方，第一个地方是数字的最前面，表示符号。第二个位置是e后面，表示指数的正负。如果出现在其他的位置一定也是非法的。
- 数字，数字没有特别的判断，本题当中没有前导0的问题。
- e只能出现一次，并且e之后一定要有数字才是合法的，123e这种也是非法的。
小数点，由于e之后的指数一定是整数，所以小数点最多只能出现一次，并且一定要在e之前。所以如果之前出现过小数点或者是e，再次出现小数点就是非法的。

作者：cheng-zhi-charles
链接：https://leetcode-cn.com/problems/valid-number/solution/python3jue-dui-jian-ji-yi-dong-de-jie-fa-by-cheng-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
```python
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        numbers = [str(i) for i in range(10)]
        n = len(s)
        
        e_show_up, dot_show_up, num_show_up, num_after_e = False, False, False, False
        
        for i in range(n):
            c = s[i]
            if c in numbers:#当前为数字，则表示数字的标识位置1
                num_show_up = True
                num_after_e = True
            elif c in ('+', '-'):#当前为正负号， 不在首位或者e后就false
                if i > 0 and s[i-1] != 'e':
                    return False
            elif c == '.':#当前为小数点，如果出现过一次小数点或者出现过e,返回false
                if dot_show_up or e_show_up:
                    return False
                dot_show_up = True
            elif c == 'e':#当前为e,如果e前没有数，或者e出现过返回False
                if e_show_up or not num_show_up:
                    return False
                e_show_up = True
                num_show_up = False
            else:
                return False
            
        return num_show_up and num_after_e
                
 
```

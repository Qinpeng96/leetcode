"""
[151. 翻转字符串里的单词](https://leetcode-cn.com/problems/reverse-words-in-a-string/)
给定一个字符串，逐个翻转字符串中的每个单词。
示例 1：

输入: "the sky is blue"
输出: "blue is sky the"
示例 2：

输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
 

说明：

无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
***
- 首先去掉左右两端的空格 lstrip(); rstrip();
- 在去点中间的多余空格
- 最后对其单词进行交换，输出到字符串中
"""
 
```python
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.lstrip(' ').rstrip(' ').split(' ')
        words = [word for word in words if word != '']
        n = len(words)
        for i in range(n//2):
            words[i], words[n-1-i] = words[n-1-i], words[i]
        return ' '.join(words)
```
其实一行代码也可以做到：

```python
    def reverseWords1(self, s: str) -> str:
        return " ".join(s.split()[::-1])

作者：jyd
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string/solution/reverse-words-in-a-string-bian-li-tian-jia-fa-by-j/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

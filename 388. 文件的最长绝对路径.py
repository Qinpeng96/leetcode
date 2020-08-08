"""
[388. 文件的最长绝对路径](https://leetcode-cn.com/problems/longest-absolute-file-path/)
假设我们以下述方式将我们的文件系统抽象成一个字符串:

字符串 "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" 表示:
#
	dir
	    subdir1
	    subdir2
	        file.ext
目录 dir 包含一个空的子目录 subdir1 和一个包含一个文件 file.ext 的子目录 subdir2 。

字符串 "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" 表示:
#
	dir
	    subdir1
	        file1.ext
	        subsubdir1
	    subdir2
	        subsubdir2
	            file2.ext
目录 dir 包含两个子目录 subdir1 和 subdir2。 subdir1 包含一个文件 file1.ext 和一个空的二级子目录 subsubdir1。subdir2 包含一个二级子目录 subsubdir2 ，其中包含一个文件 file2.ext。

我们致力于寻找我们文件系统中文件的最长 (按字符的数量统计) 绝对路径。例如，在上述的第二个例子中，最长路径为 "dir/subdir2/subsubdir2/file2.ext"，其长度为 32 (不包含双引号)。

给定一个以上述格式表示文件系统的字符串，返回文件系统中文件的最长绝对路径的长度。 如果系统中没有文件，返回 0。

说明:

文件名至少存在一个 . 和一个扩展名。
目录或者子目录的名字不能包含 .。
要求时间复杂度为 O(n) ，其中 n 是输入字符串的大小。

请注意，如果存在路径 aaaaaaaaaaaaaaaaaaaaa/sth.png 的话，那么  a/aa/aaa/file1.txt 就不是一个最长的路径。
***
- 我的思路是先分割字符串，对每一个单词进行分等级。以换行符作为分割，以Tab键作为等级，建立一个二维的列表dp.
在分割字符串的时候遇到了Tab不能直接进行比较，例如
if s[:2] == "\t"  #一直不能进入比较，因为转义符的原因，真是惭愧。

- 之后得到一个二维列表[layer, lens]，第一个元数表示这个单词的等级，第二个元素则是这个单词的长度。
- 我们还需要一个列表来记录这么多单词中，有哪些是文件格式，也就是名称内由小数点的，使用res来记录。
- 最后一步就是从二维列表中找出最长的串。有如下规律，我们每次都从res中取值，作为开始索引，从后往前找，因为文件夹的形式是从上到下的形式，我们从小向上找的好处就是，第一个找到的比当前layer小1的层就是当前层的父文件夹。并且我们还不可以将文件的名称当作文件夹，这个好办，我们在向上查找的时候，看一下要比较的索引是否在res,文件列表内，如果不在就是文件夹，可以进行比较。
- 在输出长度的时候我们还需要加上每个单词之间的斜杠，斜杠的个数就等于文件所在ayer层数。
#
	"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
	['dir', '*subdir1', '*subdir2', '**file.ext'] 	#以换行符分割，tab键替换成 " * "
	[[0, 3], [1, 7], [1, 7], [2, 8]] 				#对应索引字符串的layer 和长度
	[3]												#res, 有文件的索引
	18												#输出的最大长度
"""
```python
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        input = input.replace('\t','*')#替换Tab为星号
        input = input.split('\n')#以换行符分割
        #print(input)
        n = len(input)#计算列表的长度
        dp = []#用于存放[layer, lens]
        res = []#用于存放文件索引
        maxlen = 0
        for i in range(n):#循环遍历，计算出每个单词的层级和长度，并且把有文件的索引加入res
            layer = 0
            while input[i][0] == '*':
                input[i] = input[i][1:]
                layer += 1
            if '.' in input[i]:
                res.append(i)
            dp.append([layer,len(input[i])])

        if not res: return 0#没有文件，直接返回0
        for i in res:#对于每一个文件的索引，从后向前开始找总的路径长度
            out = dp[i][1]#当前文件的名称长度
            cnt = dp[i][0]#当前文件的层级
            for j in range(i-1, -1, -1):#从后向前找
                if j not in res and dp[j][0] < cnt:#如果前一个层级小一，且不是文件，是文件夹
                    out += dp[j][1]#长度累加
                    cnt -= 1#层级减一
            maxlen = max(maxlen, out+dp[i][0])#最后记得加上转义符的个数，其个数等于文件所在的层级
            
        return maxlen
```
"""
大佬的方法：
使用一个数组prefixSum,保存遍历过程中,已知层级的前缀字符串数。
在遍历每行数据时：
保存当前行的层级level，也就是\t的数量。

- 如果当前行为文件: 我们只要将当前文件名的长度，加上之前层级的字符串长度就行。
- 如果当前行为文件夹: 如果层级比数组长度大，我们只需在数组后面追加一个新长度; 如果层级比数组长度小，我们只需更新相应的下标为新值就行了。
代码
"""
```python
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        prefixSum = [0]
        res = 0
        for s in input.split('\n'):
            level = 0  # 当前层级
            while s[level] == '\t':
                level += 1
            sLen = len(s) - level
            # 如果是文件，比较最大值。
            if '.' in s:
                res = max(res, prefixSum[level] + sLen)
                continue
            # 如果是文件夹，将当前层级的字符串数目(包含末尾斜杆)保存。
            if level + 1 < len(prefixSum):#等级数小于层级数，意思有重复的layer了，更新layer的长度
                prefixSum[level + 1] = prefixSum[level] + sLen + 1
            else:#之前的数值个数等于等于当前的层级，直接在后面添加
                prefixSum.append(prefixSum[-1] + sLen + 1)
        return res

作者：miaoch
链接：https://leetcode-cn.com/problems/longest-absolute-file-path/solution/pythonjian-yi-jie-fa-fu-si-lu-by-miaoch/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

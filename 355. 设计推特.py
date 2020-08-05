"""
[355. 设计推特](https://leetcode-cn.com/problems/design-twitter/)
设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近十条推文。你的设计需要支持以下的几个功能：

postTweet(userId, tweetId): 创建一条新的推文
getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
follow(followerId, followeeId): 关注一个用户
unfollow(followerId, followeeId): 取消关注一个用户
示例:

Twitter twitter = new Twitter();

// 用户1发送了一条新推文 (用户id = 1, 推文id = 5).
twitter.postTweet(1, 5);

// 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
twitter.getNewsFeed(1);

// 用户1关注了用户2.
twitter.follow(1, 2);

// 用户2发送了一个新推文 (推文id = 6).
twitter.postTweet(2, 6);

// 用户1的获取推文应当返回一个列表，其中包含两个推文，id分别为 -> [6, 5].
// 推文id6应当在推文id5之前，因为它是在5之后发送的.
twitter.getNewsFeed(1);

// 用户1取消关注了用户2.
twitter.unfollow(1, 2);

// 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
// 因为用户1已经不再关注用户2.
twitter.getNewsFeed(1);
***
设计题也是束手无策啊，惭愧。
***
面向对象的思想编程：建立两个类[推特类， 用户类 ]。
推特类：包含推特的id(用于查找), 推特的时间（用于排序），指向下一条推特的指针。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200805111154495.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)

用户类：
- 用户ID(用于查找)， 用户的关注列表(集和)，用户的推特头节点(链表)，初始化自己关注自己
- 发送一条推特，包含推特id，推特时间
- 关注一个好友
- 取关一个好友（不能取关自己）	
可以看下示意图：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200805111221146.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NjUwMDI4,size_16,color_FFFFFF,t_70#pic_center)
***
接着就是大的推特这个类
- 初始化包含用户的字典(键是用户的id,键值就是这个用户类)；还有这个程序运行的时间戳。会赋值给每一个发送的推特。
- 发送推特，需要用户id,推特id。没有这个用户就创建，用户发送推特的时候需要推特id(便于查找)，时间戳(便于排序)。
- 关注好友：需要提前看这两个用户是否存在
- 取关好友：需要看被取关的用户是否存在
- 获得某一用户最近的10条推特(时间戳)：首先我们需要获得该用户的好友列表。找出这些好友发送的所有推特。
 	- 根据用户的id找到该用户这个类，从这个用户类的following列表找到所有关注者的ID。
 	- 获得这些好友的所有推特(推特ID, 推特时间戳)，放在一个列表里面 list[推特类]
 	- 对列表内的推特时间戳从大到小找十个，提出其推特的ID
 
"""

```python
import heapq

#一条推特有三个属性， 推特的序号，时间，下一条推特（链表）
class Tweet:
    def __init__(self, tid: int, time: int ):
        self.tid = tid
        self.time = time
        self.next = None

#一个用户有三个信息，用户的id, 关注列表，发过的推特（链表）
class User:
    def __init__(self, userid: int):
        self.userid = userid
        self.following = set()
        self.tweetlist = None
        self.follow(userid)#自己是关注自己的，初始化的时候就要加入
    
    def post(self, tid: int, time:int):#发送一条推特
        tweet = Tweet(tid, time)
        tweet.next = self.tweetlist
        self.tweetlist = tweet
    
    def follow(self, userid: int):
        if userid not in self.following:
            self.following.add(userid)

    def unfollow(self, userid:int):
        if userid in self.following:
            if userid != self.userid:#自己不能取关自己
                self.following.remove(userid)


class Twitter:

    def __init__(self):#初始化用户字典，和时间戳
        """
        Initialize your data structure here.
        """
        self.users = {}
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:#发送一条推特
        """
        Compose a new tweet.
        """
        if userId not in self.users:#用户不存在则创建一个用户， 发一条推特，时间戳加一
            self.users[userId] = User(userId)
        user = self.users[userId]
        user.post(tweetId, self.timestamp)
        self.timestamp += 1

        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        heap = []
        user = self.users.get(userId)

        if user:
            for uid in user.following:
                tweets = self.users[uid].tweetlist
                while tweets:
                    heap.append(tweets)
                    tweets = tweets.next
            return [twt.tid for twt in heapq.nlargest(10, heap, key = lambda twt:twt.time)]
        return []
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)

        if followerId not in self.users:
            self.users[followerId] = User(followerId)

        self.users[followerId].follow(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:#取消关注的时候，首先看被取消的人还在不在列表
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.users:
            self.users[followerId].unfollow(followeeId)
```

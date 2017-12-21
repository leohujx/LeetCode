# coding:utf-8

# 146. LRU Cache

# https://leetcode.com/problems/lru-cache/description/

'''
实现一个LRU的结构,要求put和get都要在O(1)的时间复杂度
可以利用双向链表的结构,这个结构中删除和添加节点都是O(1)的
再用一个map来记录key和Node之间的映射关系
初始化的时候用一个头结点和尾节点来进行边界的标记
'''

class Node(object):
    def __init__(self, key=-1, value=-1):
        self.key = key
        self.value = value
        self.pre = None # 前驱
        self.post = None    # 后驱

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity # 最大的空间
        self.mp = {}    # 记录Node和Key之间的关系
        self.count = 0  # 当前记录的个数
        self.head = Node()  # 头
        self.tail = Node()  # 尾
        self.head.pre = None
        self.head.post = self.tail
        self.tail.pre = self.head
        self.tail.post = None

    def addNode(self, node):    # 在头部添加节点
        tmp = self.head.post
        self.head.post = node
        node.pre = self.head
        node.post = tmp
        tmp.pre = node

    def removeNode(self, node): # 移除某个节点
        node.post.pre = node.pre
        node.pre.post = node.post

    def moveToHead(self, node): # 将某个节点添加到头部,其实就是删除某个节点然后在头部重新添加
        self.removeNode(node)
        self.addNode(node)

    def removeTail(self):       # 将最后节点删除,即尾部节点的前驱节点
        last = self.tail.pre
        self.removeNode(last)

        return last

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.mp:
            return -1
        node = self.mp[key]
        self.moveToHead(node)   # get以后记得将节点放到头部去,表示最近用过了
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.mp:
            if self.count >= self.cap: # 超过了容量
                last = self.removeTail()    # 移除尾部
                self.mp.pop(last.key)
                self.count -= 1
                # print last.key,last.value, key, value
            new_node = Node(key, value) # 添加新节点
            self.addNode(new_node)
            self.mp[key] = new_node
            self.count += 1
        else:
            node = self.mp[key] # 更新节点
            node.value = value
            self.moveToHead(node)   # 记得往头部移动!

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
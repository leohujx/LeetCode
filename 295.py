# coding:utf-8

# 295. Find Median from Data Stream

# https://leetcode.com/problems/find-median-from-data-stream/description/

'''
思路:用两个堆来做,一个大顶堆,一个小顶堆,不用实现两种,在这里我用的是小顶堆,大顶堆的实现我们可以利用
将负数放入小堆来模拟实现.

设大顶堆为maxheap, 小顶堆为minheap
假设一共add了有n个数,且n=2*k+1,那么maxheap有k+1个数,minheap有k个数
如果n=2*k, 那么maxheap有k个数,minheap也有k个数

且maxheap中的所有数都小于等于minheap中的所有数.

当放入一个数字的时候,我们首先把它放入maxheap,然后把mapheap堆顶的数放入minheap,此时如果minheap的size大于maxheap,那么
就把minheap中的堆顶元素放入maxheap,因为我们要保证minheap中的数个数小于maxheap.

那么当总数为偶数(即len(minheap) == len(maxheap)时),中位数为(minheap.top() + maxheap.top())/2
如果总数为奇数,那么中位数就为maxheap.top()

一个例子:
比如放入的序列为[1,5,3,7]
刚开始放入1,那么
maxheap [1]
minheap []
此时中位数为1

接着放入5,那么
maxheap [1]
minheap [5]
此时中位数为 (1+5)/2 = 3

接着放入3,那么
maxheap [3,1]
minheap [5]
此时中位数为3

最后放入7,那么
maxheap [3,1]
minheap [5,7]
此时中位数为(3+5)/2 = 4

空间复杂度为O(n),时间复杂度-插入为log(n),查询为O(1),所以时间复杂度为O(logn)
'''


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxheap, self.minheap = [], []

    def heapAdd(self, heap, num):   # HEAP_ADD
        n = len(heap)
        heap.append(num)
        i = n
        j = (i-1)/2
        while j >= 0 and i != 0: # 节点下沉
            if heap[j] <= num:  # 如果父节点已经小于该插入点了,那么不用再下沉(小堆)
                break
            heap[i] = heap[j]
            i = j
            j = (i-1)/2
        heap[i] = num

    def _shiftUp(self, heap, pos, n):   # 调整size为n的小堆
        while pos <= (n-1)/2:
            i = pos<<1|1
            j = i+1
            mmin = pos
            if i < n and heap[i] < heap[mmin]:
                mmin = i
            if j < n and heap[j] < heap[mmin]:
                mmin = j
            if mmin == pos:
                break
            heap[mmin], heap[pos] = heap[pos], heap[mmin]
            pos = mmin

    def heapPop(self, heap):
        n = len(heap)
        tmp = heap[0]
        heap[0] = heap[n-1] # pop就是将第一个元素用末尾元素覆盖,然后调整除了最后一个元素以外的整堆

        self._shiftUp(heap, 0, n-1)
        heap.pop()  # 这里用pop将最后一个元素排除,切记不要用什么heap[:]=heap[:-1],会很慢!直接用pop将最后一个元素排除即可
        return tmp

    def heapTop(self, heap):
        if len(heap) <= 0:
            return 0
        return heap[0]

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.heapAdd(self.maxheap, -num)
        self.heapAdd(self.minheap,-self.heapPop(self.maxheap))

        if len(self.minheap) > len(self.maxheap):
            self.heapAdd(self.maxheap, -self.heapPop(self. minheap))

        #print self.maxheap, self.minheap

    def findMedian(self):
        """
        :rtype: float
        """
        return -self.heapTop(self.maxheap)*1.0 if len(self.maxheap) > len(self.minheap) else \
    (-self.heapTop(self.maxheap) + self.heapTop(self.minheap))*1.0/2



'''
思路2:当然还可以利用heapq库函数来实现堆的操作
'''
import heapq

class MedianFinder2(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxheap, self.minheap = [], []


    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """

        heapq.heappush(self.minheap, -heapq.heappushpop(self.maxheap, -num))

        if len(self.minheap) > len(self.maxheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxheap) == 0:
            return
        return -self.maxheap[0] * 1.0 if len(self.maxheap) > len(self.minheap) else \
            (-self.maxheap[0] + self.minheap[0]) * 1.0 /2




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
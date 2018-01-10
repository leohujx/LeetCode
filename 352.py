# coding:utf-8

# 352. Data Stream as Disjoint Intervals

# https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/


'''
就是一个区间合并的过程,当一个数进来的时候,我们进行二分,选择它应该在的区间位置,
然后对原来的区间进行合并即可,注意当这个数本身就存在的时候我们忽略它
'''

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mlist = []

    def binarySearch(self, val):
        l = 0
        r = len(self.mlist) - 1
        while l <= r:
            mid = (l+r)>>1
            if self.mlist[mid].start <= val <= self.mlist[mid].end:
                return -1
            if self.mlist[mid].start > val:
                r = mid-1
            else:
                l = mid+1

        return l

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        pos = self.binarySearch(val)
        if pos == -1:
            return
        self.mlist.insert(pos, Interval(val, val)) # 在pos位置插入这个区间

        nlen = len(self.mlist)
        newList = []
        i = 1
        while i < nlen: # 区间合并
            st, ed = i-1, i-1
            while i < nlen and self.mlist[i-1].end+1 == self.mlist[i].start: # 寻找以i-1为起点的连续区间
                ed = i
                i += 1
            newList.append(Interval(self.mlist[st].start, self.mlist[ed].end)) # 合并
            if i >= nlen:    # 如果最后一个区间已经被合并,那么直接break
                break
            i += 1
        else:   # 如果没有break,说明最后一个区间没有被合并,那么我们就单独把它加入新的list
            newList.append(Interval(self.mlist[i-1].start, self.mlist[i-1].end))

        self.mlist = newList

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """

        return self.mlist



# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
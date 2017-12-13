# coding:utf-8

# 436. Find Right Interval

# https://leetcode.com/problems/find-right-interval/description/


'''
我的这个方法其实是用空间换时间,结果超过了100%的python用户= =
最简便的方法是存储每个区域的位置,然后拷贝一个副本将其按照start排序
接着遍历原数组,将end在副本中进行二分搜索.
我这方法是记录最大最小值,然后用一个数组来记录大于等于每个数字的最小的数,用另外一个map记录每个start的位置(因为题目说start
不会重复),遍历一边,O(n)即可
'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        mp = {}
        mp1 = {}
        mmin = 0x7fffffff
        mmax = -mmin
        for (i,interval) in enumerate(intervals):
            mp[interval.start] = i
            mmin = min(mmin, interval.start)
            mmax = max(mmax, interval.start)

        rmax = mmax
        for i in range(mmax, mmin-1,-1):
            if i in mp:
                rmax = i
            mp1[i] = rmax

        res = []
        for interval in intervals:
            tp = -1
            if interval.end in mp1:
                tp = mp1[interval.end]
                tp = mp[tp]
            res.append(tp)

        return res

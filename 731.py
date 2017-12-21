# coding:utf-8

# 731. My Calendar II

# https://leetcode.com/problems/my-calendar-ii/description/

'''
求至少重叠三个部分的区间
那么对于每一个start 和 end, 我们都把它放入一个books数组,对于后来的[start,end),我们比较是否
start < book.end && end > book.start,这是相交的充分必要条件,如果有那就求相交的位置,总的来说有四种位置关系
左相交
右相交
内包含
外包含
可以归纳为一种方式, [max(start,book.start) min(end, book.end)),这个就是两个区间相交的区域,把这个相交的区域放入overlaps数组
然后对于每一个进来的start和end,如果这个start和end与某个overlaps相交,那么就return false,因为overlap的意思是已经有两个
区域相交,再一次相交的话就是三个区域相交了,按照题目的说法是应该返回FALSE
'''

class MyCalendarTwo(object):

    def __init__(self):
        self.books = []
        self.overlaps = []
        pass

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for overlap in self.overlaps:
            if start < overlap[1] and end > overlap[0]:
                return False

        for book in self.books:
            if start < book[1] and end > book[0]:
                self.overlaps.append((max(start, book[0]), min(end, book[1])))

        self.books.append((start, end))

        return True



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
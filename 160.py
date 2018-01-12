# coding:utf-8


# 160. Intersection of Two Linked Lists

# https://leetcode.com/problems/intersection-of-two-linked-lists/description/

'''
经典的寻找两个链表的交点
第一个方法是很普通的,就是先找出两个链表的长度差dif,然后让长的链表先走dif步,最后让两个链表同时走,判断是否为交点.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len1 = 0
        len2 = 0
        tmp = headA
        while tmp:
            len1 += 1
            tmp = tmp.next

        tmp = headB
        while tmp:
            len2 += 1
            tmp = tmp.next

        if len1 > len2:
            headA, headB = headB, headA
            len1, len2 = len2, len1

        dif = len2 - len1
        while dif:
            headB = headB.next
            dif -= 1

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None

'''
第二个方法就很秀了,天秀.
代码就是下面很简单的代码,原理是这样.
假设有两个链表headA, headB
headA的长度为lena
headB的长度为lenb
我们假设它俩的共同长度为c
那么lena = m+c
lenb = n+c
按照代码的意思,当某个链表走到头的时候重新赋值为另外一个链表的头部,那么
a指针走的步数是 lena+lenb = m + c + n + c
b指针走的步数是 lenb+lena = n + c + m + c
仔细观察这两个算是, m+c+n=n+c+m,所以它们会在走了m+c+n的地方相遇!!且等式最后一项为c,所以这个相遇点就是第一个交点!!!
那么如果这两个链表不相交呢?那么c=0,这两个链表在走到头以后都为null,还是会相交
解决!
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a, b = headA, headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a

# coding:utf-8

# 234. Palindrome Linked List

# https://leetcode.com/problems/palindrome-linked-list/description/


'''
不用额外的空间以及O(n)的时间来判断一个链表是否为回文串
回文串的定义都知道,即正向遍历和反向遍历得到的结果相同,但是这是单链表,没有prev指针,所以不能靠这个定义
那么可以试试将前半段反过来,然后和后半段比是否一致
那么怎么定义前半段呢?首先是要找出链表的中间节点
这是个新的方法,如果按照以前,可能就是先数出来一共有几个节点,然后再遍历一遍,找到一半节点数在哪个节点.
其实有更简单和高效的方法
就跟判断链表是否有环一样,我们用两个指针,一个指针走一步,一个指针走两步,那么当后一个指针走到头的时候,第一个指针就走到了中间节点
证明:
1 奇数个节点
X X X X X
0 1 2 3 4
那么从头结点开始走起,当走了两步之后,后一个指针走到了末尾,此时第一个指针在2处,即中点处
2 偶数个节点
X X X X X X
0 1 2 3 4 5
从头结点开始,当走了3步的时候,后一个指针走到了末尾的next处,此时第一个走到了3处,即后半段的起点
所以归纳起来,这算法就是

slow, fast = head,head
while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
if fast:
    有奇数个节点
else:
    有偶数个节点

知道了一半在哪,那么判断回文子串也就不难了
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        rev = None  # 用这个指针来反转前半段的链表
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next # 反转

        if fast:
            slow = slow.next # 后半段起点

        while slow:
            if slow.val != rev.val: # 判断是否相同
                return False
            slow = slow.next
            rev = rev.next

        return True


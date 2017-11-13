# coding:utf-8


# 109. Convert Sorted List to Binary Search Tree

# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/



'''
题意:将有序列表转换为二叉搜索树
思路:
将链表的值放入数组中,然后利用数组的中值作为二叉搜索树的根,接着对数组的左右两边进行迭代构造即可
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def createBST(self, l, r, sl):
        if l > r:       # 防止比如当数组为[1,2]时,右子树的l为2,r为1,此时右子树不存在,那么返回NULL即可
            return
        if l >= r:
            return TreeNode(sl[l])

        mid = (l+r)/2
        node = TreeNode(sl[mid])
        node.left = self.createBST(l, mid-1, sl) # 递归构建左子树
        node.right = self.createBST(mid+1, r, sl)   # 递归构建右子树

        return node
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        sl = []
        while head:
            sl.append(head.val)
            head = head.next

        slen = len(sl)
        if slen <= 0:
            return []

        mid = slen/2
        tNode = TreeNode(sl[mid])
        tNode.left = self.createBST(0, mid-1, sl)
        tNode.right = self.createBST(mid+1, slen-1, sl)

        return tNode

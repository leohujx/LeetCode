# coding:utf-8

# 94. Binary Tree Inorder Traversal

# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

'''
用遍历来进行中序遍历,和144相似
左,根,右
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        return res
        """

        cur = root
        stack = []
        res = []

        while cur or stack:
            if cur:
                stack.append(cur)   # 一直往左走
                cur = cur.left
            else:
                tmp = stack.pop()   # 左走走到底了之后开始往上pop,取得一个值以后往右走
                res.append(tmp.val)
                cur = tmp.right # turn right
                pass


        return res

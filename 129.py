# coding:utf-8

# 129. Sum Root to Leaf Numbers

# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/


'''
思路:dfs,判断是否到了叶子节点即可
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, nm):
        if not root:
            return
        if not root.left and not root.right:
            self.res += nm*10+root.val
            return

        self.dfs(root.left,nm*10+root.val)
        self.dfs(root.right, nm*10+root.val)

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = 0
        self.dfs(root, 0)

        return self.res

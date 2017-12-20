# coding:utf-8

# 145. Binary Tree Postorder Traversal

# https://leetcode.com/problems/binary-tree-postorder-traversal/description/

'''
用遍历的方法来后序遍历
这里用遍历的时候其实和真正的后序遍历是相反的,先头,然后往右走,走不动的时候再往左,
可以说和后序的左右跟是完全相反的,所以输出也是相反的,故最后将输出逆序即可!
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        cur = root
        stack = []
        res = []

        while cur or stack:
            if cur:
                stack.append(cur)
                res.append(cur.val)
                cur = cur.right
            else:
                top = stack.pop()
                cur = top.left

        return res[::-1]


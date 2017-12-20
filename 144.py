# coding:utf-8

# 144. Binary Tree Preorder Traversal

# https://leetcode.com/problems/binary-tree-preorder-traversal/description/

'''
求二叉树的前序遍历,不过用dfs比较简单,这里用遍历来实现
具体看注释,同样的题目还有94, 145,分别求中序和后序
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        cur = root
        res = []    # 用来存储结果
        stack = []  # 用来当做栈

        while cur or stack:
            if cur: # 如果cur节点存在
                res.append(cur.val) # 存储该节点的值
                stack.append(cur)   # 将节点放入栈中
                cur = cur.left  # 往左走(根,左,有)
            else:
                tmp = stack.pop()   # 当某个节点不存在的时候,我们将它的父节点pop处,然后往右走一步,这之后又是(根,左,右的节奏)
                cur = tmp.right

        return res

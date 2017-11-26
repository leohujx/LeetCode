# coding:utf-8

# 508. Most Frequent Subtree Sum

# https://leetcode.com/problems/most-frequent-subtree-sum/description/


'''
思路: dfs计算子树的和即可
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, rt):
        if not rt:
            return 0
        res = rt.val + self.dfs(rt.left) + self.dfs(rt.right)
        self.rq[res] = self.rq.get(res, 0) + 1
        return res
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.rq = {}
        if not root:
            return []
        self.dfs(root)
        res = []
        # print self.rq
        tmp = sorted(self.rq.items(), key=lambda x:x[1], reverse=True)
        mmax = tmp[0][1]
        for x in tmp:
            if x[1] >= mmax:
                res.append(x[0])
            else:
                break

        return res
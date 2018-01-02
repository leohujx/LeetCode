# coding:utf-8

# 99. Recover Binary Search Tree

# https://leetcode.com/problems/recover-binary-search-tree/description/


'''
题意:二叉排序树有两个子节点的位置交换了,请找出来并重新交换回去.
解:
既然是二叉排序树,那么如果我们用中序遍历,就可以得到从小到大排序的序列,这样就能够找到交换位置的.
比如一个二叉排序树的序列为
6 3 4 5 2
说明6,2 位置错了, 把它俩进行交换.
那么找出这两个节点.
这两个节点设为first和second
我们假设有一个prev节点代表前一个节点,我们把它的值初始化为无穷小
那么当first节点为空,且prev节点的值大于等于当前节点时,first = prev, 比如上述序列的6>3,那么first.val = 6
当first节点不为空,且prev节点的值大于等于当前节点时,second = 当前节点,比如上述序列的5>2,那么seond.val = 2
最后交换这两个节点的值即可
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        cur = root
        prev = TreeNode(-0x7fffffff)
        first = None
        second = None
        q = []

        while cur or len(q) > 0:
            if cur:
                q.append(cur)
                cur = cur.left
                pass
            else:
                p = q.pop()
                if first is None and prev.val >= p.val:
                    first = prev
                if first is not None and prev.val >= p.val:
                    second = p
                # print prev, p.val
                prev = p
                cur = p.right

        first.val, second.val = second.val, first.val

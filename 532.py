# coding:utf-8

# 532. K-diff Pairs in an Array

# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/

'''
水题,直接用一个map记录下即可,注意k=0的情况.最坑的是注意k<0的情况,直接返回0即可.
'''

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mp = {}

        if k < 0:
            return 0

        for num in nums:
            mp[num] = mp.get(num, 0) + 1

        res = 0
        for key in mp:
            tmp = key + k
            if tmp == key and mp[key] >= 2: # k=0的情况
                res += 1
            elif tmp != key and tmp in  mp:
                res += 1

        return res

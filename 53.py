# coding:utf-8

# 53. Maximum Subarray

# https://leetcode.com/problems/maximum-subarray/description/

'''
题意:求最大子序列和
那么贪心一下,当和小于0时就不满足条件,否则更新最大值
注意初始条件,如果res为0,那么当数组全部为负数的话,就会出问题,所以首先将res赋值为数组中最大的值
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        sm = 0
        for x in nums:
            sm += x
            if sm < 0:
                sm = 0
            else:
                res = max(res, sm)

        return res
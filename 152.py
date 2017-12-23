# coding:utf-8

# 152. Maximum Product Subarray

# https://leetcode.com/problems/maximum-product-subarray/description/

'''
求最大子序列的积
和最大子序列的和不同,最大子序列当和为负数的时候,就可以重新赋值计算,但是当积为负数的时候,后面也许还有一个负数,这样负负就得正了.
所以在这个问题里面,我们需要同时维护当前的最大值和最小值,分别为mmax, mmin
注意当我们遇到负数的时候,mmax和mmin的身份就调换了,即 mmax, mmin = mmin, mmax
维护最值的时候取  最值*当前数, 当前数  中的最值即可
'''

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nlen = len(nums)

        if not nums:
            return 0

        mmax = nums[0]
        mmin = nums[0]

        res = nums[0]

        for num in nums[1:]:
            if num < 0:
                mmax, mmin = mmin, mmax

            mmax = max(num, mmax*num)
            mmin = min(num, mmin*num)

            res = max(mmax, res)

        return res


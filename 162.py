# coding:utf-8

# 162. Find Peak Element

# https://leetcode.com/problems/find-peak-element/description/

'''
找一个峰值(nums[i-1]<nums[i]>nums[i+1])
这可以用二分,,,感觉挺神奇..
因为题目要找任意一个峰值即可,所以我们可以用二分来确定这个峰值
mid = (l+r)/2
当nums[mid] < nums[mid+1]时,此时说明有一个峰值肯定是在[mid,nlen)这边,所以l = mid+1
否则的话是在(0, mid]这边,无论如何,l肯定是一个可行解
'''

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nlen = len(nums)
        l = 0
        r = nlen-1

        while l<r:
            mid = (l+r)>>1
            if nums[mid] < nums[mid+1]:
                l = mid+1
            else:
                r = mid

        return l
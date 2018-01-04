# coding:utf-8

# 33. Search in Rotated Sorted Array

# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

'''
对于一个部分倒序的有序序列,为了二分查找某个数target,我们有以下这么几种情况
假设左边界l,右边界r,mid=(l+r)/2
当nums[l] <= nums[mid]时,分两种情况
1.当 nums[l] <= target <= nums[mid]时,即目标数在[l,mid]区间中,且[l,mid]是递增区间,那么就在这个区间搜索即可-> r = mid-1
2. 即1不成立时,说明此时target在区间外面(后面)--> l = mid + 1
当nums[l] > nums[mid]时,说明mid落在倒序的部分,此时也分两种情况
1. 当nums[mid]<=target<=nums[r]时,即目标数在[mid,r]区间中,且[mid,r]是递增区间,那么就在这个区间搜索即可--> l=mid+1
2. 即1不成立,说明此时target在区间外面(前面) --> r = mid-1
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1

        while l <= r:
            mid = (l+r) >> 1
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
                pass
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1

        return -1
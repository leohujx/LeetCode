# coding:utf-8

#  42. Trapping Rain Water

# https://leetcode.com/problems/trapping-rain-water/description/



'''
思路:其实知道思路了以后这种用空间换时间的方法就很好想了.
直接的暴力思想就是找每个柱子左右两边的最高的高度,然后取较小的最高高度-当前柱子的高度.最后的答案就是它们的和
那么用mmaxLeft[i]来表示i左边最高的柱子高度
mmaxRight[i]来表示i右边最高的柱子高度
正反循环一遍即可
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        hlen = len(height)
        mmaxLeft = [0]*hlen
        mmaxRight = [0]*hlen

        if hlen == 0:
            return 0

        mmaxLeft[0] = 0
        mmax = height[0]
        for i in range(1, hlen):
            mmax = max(mmax, height[i])
            mmaxLeft[i] = mmax

        mmaxRight[hlen-1] = 0
        mmax = height[hlen-1]

        for i in range(hlen-2,-1, -1):
            mmax = max(mmax, height[i])
            mmaxRight[i] = mmax

        ans = 0
        for i in range(1, hlen-1):
            ans += min(mmaxLeft[i], mmaxRight[i]) - height[i]

        return ans

'''
还有一种就是用空间复杂度为O(1)的方法来,既然我们要维护左右两边的最大值,那么我们也可以用两个指针遍循环遍计算
用maxLeft来表示左边的最大值,用maxRight来表示右边的最大值,那么让一个指针指向开头,一个指向末尾
则如果左边的柱子高度小于右边的,就利用左边的柱子来计算,如果左边柱子高度大于maxLeft,那么更新maxLeft,否则计算maxLeft-height[i]
右边情况同理
'''

class Solution(object):
    def trap(self, A):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(A) - 1
        res = 0
        maxL, maxR = 0, 0
        while l <= r:
            if A[l] <= A[r]:
                #use left height as the wall
                if (A[l] >= maxL):
                    maxL = A[l]
                else:
                    res += maxL - A[l]
                l += 1
            else:
                if A[r] >= maxR:
                    maxR = A[r]
                else:
                    res += maxR - A[r]
                r -= 1
        return res
# coding:utf-8

# 416. Partition Equal Subset Sum

# https://leetcode.com/problems/partition-equal-subset-sum/description/


'''
01背包啊!
状态转移
dp[v] = (dp[v] or dp[v-num])
'''

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ssum = sum(nums)
        if ssum & 1 == 1: # 奇数,直接返回False
            return False

        hf = ssum/2
        nlen = len(nums)

        mmax = max(nums)

        if mmax > hf:       # 最大值大于一半,返回False
            return False

        dp = [0]*(hf+10)

        dp[0] = 1

        for num in nums:
            for cap in range(hf, num-1, -1):
                dp[cap] = dp[cap-num] or dp[cap]

        return dp[hf] == 1

# coding:utf-8

# 518. Coin Change 2

# https://leetcode.com/problems/coin-change-2/discuss/

'''
思路一:利用dp,其中dp[i]代表金钱为i时利用coins能够组成的方案总数,其中dp[0]=1
那么dp[j] = dp[j] + dp[j-coins[i]]
'''

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount+10)
        dp[0] = 1
        clen = len(coins)
        for i in range(clen):
            for j in range(coins[i], amount+1):
                dp[j] += dp[j-coins[i]]

        return dp[amount]


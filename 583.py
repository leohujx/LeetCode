# coding:utf-8

# 583. Delete Operation for Two Strings

# https://leetcode.com/problems/delete-operation-for-two-strings/description/


'''
题意:给定两个字符串,求至少几步能够把两个字符串变为一样,每一步可以在任意一个字符串中删减一个字母.
思路:其实这道题就是求两个字符串的最长公共子序列LCS 然后答案就是len1+len2-2*LCS
最长公共子序列递推:
if w1[i-1] == w2[j-1]: dp[i][j] = dp[i-1][j-1] +1
else dp[i][j] = max(dp[i-1][j], dp[i][j-1])

如果是最长公共子串那么:
if w1[i-1] == w2[j-1]: dp[i][j] = dp[i-1][j-1]+1
else dp[i][j] = 0
'''

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #dp[i][j] # a的长为i,b的长为j时的最长公共子串

        len1 = len(word1)
        len2 = len(word2)
        if len1 == 0 or len2 == 0:  # 注意为0的情况
            return len2 if len1 == 0 else len1

        dp = [[0 for i in range(len2+2)] for j in range(len1+2)]    # 注意横纵坐标！

        for i in range(1, len1+1):
            for j in range(1, len2+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + (word1[i-1] == word2[j-1]))

        com = dp[len1][len2]
        return len1+len2-2*com

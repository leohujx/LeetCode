# coding:utf-8

# 397. Integer Replacement

# https://leetcode.com/problems/integer-replacement/description/

'''
在n向1的转变过程中,如果n为偶数,那一定是/2;当n为奇数的时候,n+1或者n-1,这两个都有可能.
所以我们用dfs来进行搜索,搜索过程中取n+1和n-1小的那个.注意用记忆化搜索,这样可以节省大量的时间.
'''
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        check = {}

        def dfs(num):
            if num in check:
                return check[num]
            if num == 1:
                return 0
            if num % 2 == 0:
                check[num] = dfs(num/2)+1
                return check[num]
            check[num] = min(dfs(num+1)+1, dfs(num-1)+1) # 取小的那个方案
            return check[num]

        return dfs(n)
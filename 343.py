# coding:utf-8

# 343 Integer Break

# https://leetcode.com/problems/integer-break/description/

'''
这道题目求组成某个数的最大积是多少.
我们举几个例子来分解下就能发现规律
2 1 1  -  1
3 2 1  - 2
4 2 2  - 4
5 3 2 - 6
6 3 3 - 9
7 3 2 2 - 12
8 3 3 2  - 18
9  3 3 3 - 27
10 3 3 2 2 - 36
11 3 3 3 2 -54

可以发现,除了2, 3, 4这几个特殊以外,其他的都是由3或者2组成的,那么说明最终答案肯定是3和2的积,
那么贪心下发现,肯定是3越多越好啊,积就越大,所以我们首先从n中抽3,条件是此时n>4,因为除了3,我们只允许最后的序列中有2

'''

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4

        res = 1
        while n - 3 > 1:    # 不断抽出3
            res *= 3
            n -= 3

        res *= n

        return res
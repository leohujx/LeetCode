# coding:utf-8

# 329. Longest Increasing Path in a Matrix

# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/


'''
感觉这道题目并不难啊....
不知道为啥做了n久没写出来..
最后看了一眼真的很简单啊啊啊,,不就是一个记忆化搜索吗...T_T
'''


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])

        mp = {}
        dr = [[-1,0], [1,0],[0,1],[0,-1]] # 搜索的四个方向

        def check(x, y):
            if x < 0 or x >=n or y < 0 or y >= m:
                return False
            return True

        def dfs(x, y):
            if (x, y) in mp:    # 记忆化
                return mp[(x,y)]

            mmax = 1
            for d in dr:    # 对于每个点我们取它能够dfs到的最大值
                xx = x+d[0]
                yy = y+d[1]
                if check(xx, yy) is False or matrix[xx][yy] <= matrix[x][y]:
                    continue
                tmp = dfs(xx, yy) + 1 # 后续值+当前值
                mmax = max(mmax, tmp)

            mp[(x,y)] = mmax # 记录下来
            return mmax


        res = 1
        for i in range(n):  # 遍历每一个点
            for j in range(m):
                tmp = dfs(i, j)
                res = max(res, tmp)

        return res

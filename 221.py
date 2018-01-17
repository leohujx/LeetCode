# coding:utf-8

# 221. Maximal Square


# https://leetcode.com/problems/maximal-square/description/


'''
是道好题目,之前好像也碰到过.
让找全为1的子正方形
那么其实这是道dp的题目
如果按照一般的做法复杂度太高
那么用dp就可以做到n*m的复杂度
我们用dp[i][j]来表示以(i,j)为矩阵右下角的最大正方形的边长
对于边界情况来说, 以(i,0)或者(0,j)为右下角的最大正方形肯定为0或者1,这就看这个坐标上的值为0还是1了,即dp[i][j] = matrix[i][j]
对于非边界情况来说,即i>0&&j>0,如果matrix[i][j] == 0,那么dp[i][j]肯定也为0
那么就剩当 matrix[i][j] = 1的情况
比如
0 1
1 1
对于(1,1)这个点来说,此时矩阵的边长大小取决于它左边,上面和左上角的点已经形成的正方形边长
再比如
1 1 1 1
1 1 1 1
1 1 1 1
对于最右下角的点来说,上面点形成的正方形边长为2,左边的为3,左上角的为2,根据观察这个右下角的点能够形成的最大正方形边长为3
也就是min(2,3,2)+1,取这三个参考点的最小值,然后加一
可以这么证明,因为取的是最小的边长,我们可以把左上角形成的矩阵看为最小的那个正方形X,那么上面点形成的矩阵肯定是包含在这个X中,
只是最右边多出了一块
同理,左面形成的矩阵肯定也是包含在这个X中,只是最下面多出了一块
那么右边多出了一块,下面多出了一块,再加上此时最右下角多出的一块,那么拼起来的图形肯定也是正方形.
'''

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        n = len(matrix)
        m = len(matrix[0])

        res = 0

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    matrix[i][j] = int(matrix[i][j])
                elif matrix[i][j] == '0':
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                res = max(res, matrix[i][j])

        return res*res


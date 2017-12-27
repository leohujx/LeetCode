# coding:utf-8

# 36. Valid Sudoku

# https://leetcode.com/problems/valid-sudoku/description/

'''
检查已填入数独的棋盘是否符合规则,注意只检查已经填入的,不要求一定要有解
那么检查行,列,块即可, 行和列都很简单,搞一个二维数组即可,对于块
本来我是弄了一个三维数组分别为[i/3][j/3][num]来检测是否重复,对于每一个块,(i/3,j/3)都是唯一的
后来发现有个更省空间的,就是[i//3*3+j/3][num]即可,用二维来替代三维,能做到每个块的计算结果都不同
'''

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [[0 for i in range(10)] for j in range(10)]
        cols = [[0 for i in range(10)] for j in range(10)]

        sqls = [[0 for i in range(10)] for j in range(10)]


        nlen = len(board)
        mlen = len(board[0])

        for i in range(nlen):
            for j in range(mlen):
                tmp = board[i][j]
                if tmp == '.':
                    continue
                tmp = int(tmp)
                if rows[i][tmp] == 1:
                    return False
                if cols[j][tmp] == 1:
                    return False
                if sqls[i//3*3+j/3][tmp] == 1:
                    return False

                rows[i][tmp] = 1
                cols[j][tmp] = 1
                sqls[i//3*3+j/3][tmp] = 1

        return True

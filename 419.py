# coding:utf-8

# 419. Battleships in a Board

# https://leetcode.com/problems/battleships-in-a-board/description/

'''
因为X都是横着或者竖着 连着的(),所以我们从左向右,从上往下遍历,只要这个格子为X并且它上面和左边不是X就是一个新的
battleshipe
'''

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board:
            return 0
        rows = len(board)
        cols = len(board[0])
        res = 0
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == '.':
                    continue
                if i > 0 and board[i-1][j] == 'X':
                    continue
                if j > 0 and board[i][j-1] == 'X':
                    continue
                res += 1

        return res

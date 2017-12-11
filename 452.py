# coding:utf-8

#  452. Minimum Number of Arrows to Burst Balloons

# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/


'''
简单的贪心,将点按照end端进行从小到大排序,然后每次取end,看最多能够覆盖几个点,这样的策略是最优的
'''

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        if not points:
            return 0

        points = sorted(points, key=lambda x:x[1])

        rt = points[0][1]
        res = 1

        for point in points[1:]:
            if point[0] <= rt <= point[1]:
                continue
            rt = point[1]
            res += 1

        return res
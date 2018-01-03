# coding:utf-8

# 667. Beautiful Arrangement II

# https://leetcode.com/problems/beautiful-arrangement-ii/description/

'''
我的构造思路:
当k为奇数,比如n=10, k=5的时候,我用两个指针分别指向1和10,然后分别取首和尾,1 10 2 9 ....
一直这样取5个数,即1 10 2 9 3, 然后这里的差为9,8,7,6 后面只能是有一个差了,那么就跟 顺序序列,即 1 10 2 9 3 4 5 6 7 8
当k为偶数的时候也差不多,如k=6
先取6个数 1 10 2 9 3 8,差分别为9,8,7,6,5 后面也只能有一个差,也跟顺序序列,只不过相反 1,10,2,9,3,8,7,6,5,4
'''

class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = []

        i = 1
        j = n
        p = 0

        while True:
            res.append(i)
            p += 1
            i += 1
            if p >= k:
                break
            res.append(j)
            p += 1
            j -= 1
            if p >= k:
                break

        if k % 2 == 1:
            res.extend([p for p in range(i, j+1)])
        else:
            res.extend([p for p in range(j, i-1, -1)])

        return res


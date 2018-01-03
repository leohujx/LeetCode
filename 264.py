# coding:utf-8

# 264. Ugly Number II

# https://leetcode.com/problems/ugly-number-ii/description/

'''
思路:既然丑数都是由2,3,5的倍数组成的,那么我们来观察下它的某个序列
[1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24]
可以看出,这个列表中的每个数字(除了1),都是由前面的数*2,*3,*5得来的,所以我们可以这么做.
用t2,t3,t5表示当前生产的数字下标,初始化都为0, 序列初始也只有一个1,那么取mmin = min(2*res[t2], 3*res[t3], 5*res[t5])
当mmin与2*res[t2]或者3*res[t3]或者5*res[t5]相等的时候,那么为了下次不产生同样的数,那么t2+=1或者t3+=1或者t5+=1
注意mmin有可能同时等于多个数,比如同时等于2*res[t2]或者3*res[t3],那么此时t2和t3都得+1
'''

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        t2, t3, t5 = 0, 0, 0

        for i in range(1, n):
            tp = min(2*res[t2], 3*res[t3], 5*res[t5])
            if tp == 2*res[t2]:
                t2 += 1
            if tp == 3*res[t3]:
                t3 += 1
            if tp == 5*res[t5]:
                t5 += 1
            res.append(tp)

        return res[n-1]
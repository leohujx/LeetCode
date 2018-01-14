# coding:utf-8

# 166. Fraction to Recurring Decimal

# https://leetcode.com/problems/fraction-to-recurring-decimal/description/


'''
经典的分数化小数问题
首先注意分子分母的正负性,如果是负数的话,我们统一化成正数,最后来加-即可
那么怎么计算循环节呢
模拟2/3的情况来看,先是得出整数部分为2/3取整
然后对于小数部分,就是2*10/3取整,之后除数变为20%3的值2,接着再是2*10/3,,往复如此
那么我们怎么知道循环节的部分呢
我们用一个map来记录每次出现的除数,如果除数重复了,那么之后必定是循环的,但是怎么确定循环节的位置呢,因为有些小数
是比如0.234565656....循环是56,我是这么做的
用map来记录的时候不是单纯的只用1来记录是否出现,我记录每次除数出现的位置,如果再次出现了,那么就找到了以前第一次循环出现的地方,
这样就能找到循环节的位置了

'''

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator % denominator == 0:
            return str(numerator/denominator)

        flag = 0
        if numerator < 0 and denominator < 0:
            numerator, denominator = -numerator, -denominator
        elif numerator < 0:
            numerator = - numerator
            flag = 1
        elif denominator < 0:
            denominator = -denominator
            flag = 1

        res = str(numerator/denominator) + "."


        numerator = numerator % denominator

        mp = {}
        val = -1
        lp = len(res) + 1   # 当前位置
        while numerator:
            numerator *= 10
            if mp.get(numerator, 0) > 0:
                val = mp.get(numerator) # 找到第一次出现的位置
                break
            mp[numerator] = lp  # 记录当前位置
            res += str(numerator/denominator)
            numerator = numerator % denominator
            lp = len(res) + 1   # 更新

        if val != -1:
            rlen = len(res)
            newr = ""
            for i in range(rlen):
                j = i + 1
                if j == val:    # 找到了循环节,那么就在前面加(
                    newr += "("
                newr += res[i]
            newr += ")"
            res = newr

        if flag == 1:
            res = "-" + res # 本来是负数
        return res



# coding:utf-8

# 357. Count Numbers with Unique Digits

# https://leetcode.com/problems/count-numbers-with-unique-digits/description/

'''
思路: 本来我一直想减去相同值个数来着,,结果直接加不同的个数更简单..
有一点,如果n>10, 那么直接置n为10,因为n>10的话肯定是有重复的
所以我们逐位相加,第一位最多九个(1-9),第二位也是9个(0+除去第一位),第三位8个,第四位7个......
'''


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        fac = [9,9,8,7,6,5,4,3,2,1]
        n = n if n <= 10 else 10

        res, pro = 1, 1

        for i in range(n):
            pro *= fac[i]
            res += pro

        return res

s = Solution()

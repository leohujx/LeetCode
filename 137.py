# coding:utf-8

# 137. Single Number II

# https://leetcode.com/problems/single-number-ii/description/


'''
这道题目以前做到过,当时就觉得做法很赞,印象比较深刻,所以基本做出来了,有一点没搞出来就是当num超过int的时候,因为python没有
所谓的32位,不像C语言一样能够自动截断,所以当超过int的时候,应该减去2^32转换为int类型

思想就是用位来思考,对于每个数字的第i位,相同数字的该位肯定相同,那么按照这个位是否为1,我们将数组中的数字
分为两个集合,一个就是第i位为1,另外一个就是第i位为0.
对于第i位为1的,说明这个数字拥有第i位的1,如果第i位为1的数字个数为3的整数倍+1,说明只出现一次的那个数字的第i位也为1
因为相同数字的第i位肯定相同,所以如果个数为3倍+1,那么说明单独出现一次的那个数字肯定出现在这个集合, 也说明这个数字的第i
位为1.
遍历32位整数,将单独出现的这个数字逐位还原即可.

'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def convert(num):
            if num > 0x7fffffff:
                num -= (2**32)
            return num

        res = 0
        lt = 0

        lt_val = 0

        for i in range(32):
            lt = 0
            lt_val = 0
            x = (1<<i)
            for num in nums:
                if num & x: # 如果第i位为1
                    lt += 1

            if lt % 3:  # 对3不整除,准确的来说是3倍加1
                res |= x

        return convert(res)

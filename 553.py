# coding:utf-8

# 553. Optimal Division

# https://leetcode.com/problems/optimal-division/description/


'''
对于a/b/c/d/e....来说,如果要找到一个加括号方案使得这个算式值最大.
那么对于a/b来说,这一步是不可少的,如果b跟a结合,那么就是a/b*(.....),如果b跟后面的结合,那么
也可以写成a/(b/c/d....) = a/b*(....),省略号我们可以用Y来代替,那么要使得这个算式最大,那么
Y = c*d*e.... a/(b/c/d/e) = (a*c*d*e...)/b
所以所有的答案都是 a/(b/c/d/e....)的格式
'''

class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nlen = len(nums)
        if nlen == 1:
            return str(nums[0])
        if nlen == 2:
            return str(nums[0]) + "/" + str(nums[1])

        res = ""
        res = str(nums[0]) + "/("
        for i in range(1, nlen):
            res += str(nums[i]) + ("/" if i != nlen-1 else "")

        res += ")"

        return res
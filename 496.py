# coding:utf-8

# 496. Next Greater Element I

# https://leetcode.com/problems/next-greater-element-i/description/

'''
题意:给你两个数组findNums和nums,其中findNums是nums的一个子集,问在findNums中取一个数,我们需要在nums中找到这个数的右边比它
大的数.
思路:第一种解法就直接用mp来标记下nums中每个数字出现的位置,然后遍历findNums,对于每个数字,从mp[x]中开始往右寻找第一个比它
大的,复杂度 O(n*n)
'''
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        flen = len(findNums)
        nlen = len(nums)
        mp = {}
        res = []
        for i, x in enumerate(nums):
            mp[x] = i
        for x in findNums:
            pos = mp[x]
            for i in range(pos+1, nlen):
                if nums[i] > x:
                    res.append(nums[i])
                    break
            else:
                res.append(-1)

        return res


'''
第二种思路:利用一个队列来维护在nums数组中某个数距离它最近的比它大的数,
复杂度: O(n)
'''

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        s = []
        mp = {}
        for x in nums:
            while len(s) and s[-1] < x: # 此时的数比之前在队列中的都要大,那么就记录下来
                mp[s.pop()] = x
            s.append(x)

        for x in findNums:
            res.append(mp.get(x, -1))   # 取出

        return res

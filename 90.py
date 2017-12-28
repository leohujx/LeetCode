# coding:utf-8

# 90. Subsets II

# https://leetcode.com/problems/subsets-ii/description/


'''
题意为取一个有重复元素的所有不重复子集.
我自己的解法就不拿出来献丑了.._(:зゝ∠)_

有两种比较大众的解法.
一种是用递归
首先需要对原数组排序,这样能够排除重复的元素
然后开始递归,注意在保持答案的时候需要深复制,要不然append进去的元素会在不断变化
'''

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nlen = len(nums)
        def dfs(start, tmp):

            res.append(tmp[:])
            for i in range(start, nlen):
                if i > start and nums[i] == nums[i-1]: # 相等的就不要再重复计算
                    continue
                tmp.append(nums[i])
                dfs(i+1, tmp)
                tmp.pop()

        nums.sort()
        dfs(0, [])

        return res

'''
第二种是直接用循环,如果上一个数和当前的数相等,那么只往上一轮得到的子集中加入数字,
否则从头开始加入.
'''

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]

        size, start = 0,0

        nums.sort()
        nlen = len(nums)

        for i in range(nlen):
            start = size if i > 0 and nums[i] == nums[i-1] else 0
            size = len(res)
            # print i, size, nums[i]
            for j in range(start, size):
                tmp = res[j]
                # tmp.append(nums[i])
                # print tmp, tmp+[nums[i]]
                res.append(tmp+[nums[i]])
            # print res
        return res


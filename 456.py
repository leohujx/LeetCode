# coding:utf-8

# 456. 132 Pattern

# https://leetcode.com/problems/132-pattern/description/

'''
这个解法不会啊,学习一下!
我们要找一个序列,使得 s1 < s3 < s2
那么对于一个序列,我们只要找到最可能符合条件的那个序列,如果最可能的序列都不行,那么肯定不存在132这种序列.
什么叫做最可能的符合序列呢,就是当s2最大的时候,且s3小于s2,然后来了一个数小于s3,那么存在s1 < s3 < s2
这里我们用到了栈,栈在这里维护的是可能的s2的值,栈中的数据是递减的,当某个数大于栈中的值时会被一直pop,
最后一个pop的数为s3,此时s2就是栈顶的元素.
s1是遍历中每次遇到的数组元素
举个例子,比如数组
i = 6, nums = [ 9, 11, 8, 9, 10, 7, 9 ], S1 candidate = 9, S3 candidate = None, Stack = Empty
i = 5, nums = [ 9, 11, 8, 9, 10, 7, 9 ], S1 candidate = 7, S3 candidate = None, Stack = [9]
i = 4, nums = [ 9, 11, 8, 9, 10, 7, 9 ], S1 candidate = 10, S3 candidate = None, Stack = [9,7]
i = 3, nums = [ 9, 11, 8, 9, 10, 7, 9 ], S1 candidate = 9, S3 candidate = 9, Stack = [10]
i = 2, nums = [ 9, 11, 8, 9, 10, 7, 9 ], S1 candidate = 8, S3 candidate = 9, Stack = [10,9] We have 8<9, sequence (8,10,9) found!
'''

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        mlist = []
        nlen = len(nums)

        s3 = -0x7fffffff
        for i in range(nlen-1, -1, -1):
            if nums[i] < s3:
                return True
            while mlist and nums[i] > mlist[-1]:
                s3 = mlist[-1]
                mlist.pop()

            mlist.append(nums[i])

        return False
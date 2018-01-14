# coding:utf-8

# 75. Sort Colors

# https://leetcode.com/problems/sort-colors/description/


'''
最直白的想法就是先循环一次,把0有多少个,1有几个,2有几个全部数出来,然后再来一次循环将0填在一起,1填在一起,2填在一起.
题目中要求如果只用一次循环应该怎么办
可以用下面的方法
我们先指定放置的策略,为000...111....222
然后使用三个指针,一个是指向末尾,代表2序列放置的起点左边界sd,一个指向开头,代表0序列放置的右边界zr,那么剩下的空间就是放置1了
利用一个循环i,当nums[i]==2并且i是小于2序列的起点左边时,那么就将起点sd和i处的值互换位置,并且将sd--,然后继续比较
0也是一个道理,条件为nums[i]==1并且i是大于0序列的右边界,那么i和zr互换位置,并且zr++,然后继续比较
这样最后就会将0赶到开头,2移到末尾,那么剩下的1自然就跑到了中间
'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nlen = len(nums)
        i = 0
        zr = 0
        sd = nlen-1
        for i in range(nlen):
            while nums[i] == 2 and i < sd:  # 如果i为2并且i<sd
                nums[i], nums[sd] = nums[sd], nums[i]
                sd -= 1

            while nums[i] == 0 and i > zr:  # 如果i为0并且i>zr
                nums[i], nums[zr] = nums[zr], nums[i]
                zr += 1





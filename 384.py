# coding:utf-8

# 384. Shuffle an Array

# https://leetcode.com/problems/shuffle-an-array/description/


'''
主要是怎么进行shuffle
参考https://yjk94.wordpress.com/2017/03/17/%E6%B4%97%E7%89%8C%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%A7%BF%E5%8A%BF-knuth-shuffle%E7%AE%97%E6%B3%95/
我们可以知道普通的shuffle方法,就是对于当前的i,我们随机产生一个数j,使得nums[i], nums[j]交换位置
而从参考的文章中可以看出,这个方法不是完全随机的,不同情况之间的几率不相同
所以有个改进的放法叫做knuth shuffle,即对于i, 产生的随机数j是小于i的,这样可以保证完全随机,
当然也可以产生的随机数j是大于i的(i + random.randint(n-i))

'''

import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self._origin = nums[:]


    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.nums = self._origin[:]
        return self.nums


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        nlen = len(self.nums)
        for i in range(nlen):
            j = random.randint(0, i)    # 产生小于j的随机数
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

        return self.nums



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
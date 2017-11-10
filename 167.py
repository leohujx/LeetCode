# coding:utf-8

# 167 Two Sum II - Input array is sorted

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/


'''
思路: 在一个有序数组中求两个数的下标,使得这两个数的和为target
那么除了常规使用map之外,因为这里是有序的,那么我们可以用首尾指针来进行移动,当结果比target大时尾指针向前移动,
否则首指针往后移动
'''

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        while i < j:
            res = numbers[i] + numbers[j]
            if res == target:
                break
            if res > target:
                j -= 1
            elif res < target:
                i += 1

        return [i+1, j+1]
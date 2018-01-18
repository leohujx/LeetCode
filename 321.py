# coding:utf-8

# 321. Create Maximum Number

# https://leetcode.com/problems/create-maximum-number/description/


'''
这道题目比较麻烦,具体看注释,总的来说分为三步
1.从两个数组中分别取i个和k-i个数,组成最大的数组
2.将第一步中组成的两个最大数组合并为一个最大数组
3.遍历i,在最大数组中选取最大值
'''

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def makeArray(nums, k): # 组装最大数组
            tmp = [-1] * k
            i, j = 0,0
            n = len(nums)
            for i in range(n):
                # 当目前数组中所剩下数字的个数 大于 实际所需要的凑成k个的数字,即n-i > k-j,也就是满足
                # 剩下的数必须能够凑成元素为k个的最大数组
                # 并且当前的nums[i]大于数组中的后缀时(可进行替换),其实相当于一个插入排序一样
                # 比如此时tmp = [6,5,1], nums[i] = 6,那么替换后就为 tmp = [6,6]
                while n-i > k-j and j > 0 and nums[i] > tmp[j-1]:
                    j -= 1
                if j < k: # 进行替换
                    tmp[j] = nums[i]
                    j += 1

            return tmp

        def merge(arr1, arr2, k): # 合并
            tmp = []
            i, j = 0,0
            for r in range(k):
                if greater(arr1, i, arr2, j): # arr1[i] > arr2[j]
                    p = arr1[i]
                    i += 1
                else:
                    p = arr2[j]
                    j += 1
                tmp.append(p)
            return tmp

        def greater(arr1, i, arr2, j): # 选出更大的数
            n = len(arr1)
            m = len(arr2)

            while i < n and j < m and arr1[i] == arr2[j]: # 如果相同,则往后比较
                i += 1
                j += 1

            return j == m or (i < n and arr1[i] > arr2[j]) # arr1[i]比较大

        res = [0] * k
        n = len(nums1)
        m = len(nums2)

        i = max(0,k-m)
        while i <= n and i <= k: # 枚举i, i的范围在[max(0,k-m), min(n,k)]
            tmp = merge(makeArray(nums1, i), makeArray(nums2, k-i), k) # 得到最大数组
            if greater(tmp, 0, res, 0): # 将得出的最大数组和答案res进行比较,如果比res大那么进行赋值替换
                res = tmp[:]
            i += 1

        return res


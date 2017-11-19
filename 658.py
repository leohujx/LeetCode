# coding:utf-8

# 658. Find K Closest Elements


# https://leetcode.com/problems/find-k-closest-elements/description/

'''
思路1: 将数字x用二分插入原数组中,使得原数组仍有序,然后用两个指针从插入的位置开始往左右扩展,
当左边的数字和x的差较小的时候就取左边的值,并将左边的指针往左边走,反之则反,一共取k个数即可
'''

class Solution(object):
    def binarySearch(self, arr, x):
        l = 0
        r = len(arr)
        while l<r:
            mid = (l+r)>>1
            if arr[mid] > x:
                r = mid
            else:
                l = mid+1

        return r
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        pos = self.binarySearch(arr, x)
        arr = arr[:pos] + [x] + arr[pos:]
        res = []
        i = pos-1
        j = pos+1
        arr_len = len(arr)
        while i >=0 and j < arr_len:
            dif1 = abs(arr[i] - x)
            dif2 = abs(arr[j] - x)
            if dif1 <= dif2:
                res.append(arr[i])
                i -= 1
            else:
                res.append(arr[j])
                j += 1
            k -= 1
            if k <= 0:
                break
        while k and i >= 0:
            res.append(arr[i])
            i -= 1
            k -= 1
        while k and j < arr_len:
            res.append(arr[j])
            j += 1
            k -= 1
        res.sort()
        return res


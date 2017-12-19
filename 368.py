# coding:utf-8

# 368. Largest Divisible Subset

# https://leetcode.com/problems/largest-divisible-subset/description/

'''
这道题目可以借最长递增子串的思想,然后记录路径
先复习下最朴素的最长递增子串O(n^2)的算法
对于一个数组a[],我们用dp[i]来表示以第i个数字结尾的最长递增子串,初始化的情况下dp[i] = 1
当遍历到某个数i的时候,我们遍历其前面的所有j∈[0,i),如果存在 a[i] > a[j]情况下说明i,j可以作为递增串,
不过这里还有一个条件,就是此时还得满足 dp[i] < dp[j] + 1,因为我们总是要取最大的
比如有个序列为 [1,2,-1,72],可以看出来dp[0] = 1, dp[1] = 2, dp[2] = 1
那么当i=3时,a[i]=72, dp[i]=1
遍历[0,3)
j = 0, a[i] > a[j] && dp[i] < dp[j]+1 ==> dp[i] = dp[j] + 1 = 1 + 1 = 2
j = 1 ,a[i] > a[j] && dp[i] < dp[j]+1 ==> dp[i] = dp[j] + 1 = 2 + 1 = 3
j = 2, a[i] > a[j]但此时 dp[i](3) > dp[j]+1(1+1=2),所以不成立
最后输出最长的为3

这道题目也一样,比如
[1,2,4,8,9,72]
可以看出dp[0] = 1(1), dp[1] = 2(1,2), dp[2] = 3(1,2,4), dp[3] = 4(1,2,4,8), dp[4] = 2(1,9)
那么当i=5是,dp[i] = 1
遍历[0,5)
j = 0, a[i]%a[j] == 0 && dp[i] < dp[j]+1 ==> dp[i] = dp[j] + 1 = 1 + 1 = 2
j = 1, a[i]%a[j] == 0 && dp[i] < dp[j]+1 ==> dp[i] = dp[j] + 1 = 2 + 1 = 3
j = 2, a[i]%a[j] == 0 && dp[i] < dp[j]+1 == > dp[i] = dp[j] + 1 = 3 + 1 = 4
j = 3, a[i]%a[j] == 0 && dp[i] < dp[j]+1 == > dp[i] = dp[j] + 1 = 4 + 1 = 5
j = 4,a[i]%a[j] == 0 但是 dp[i] > dp[j]+1,所以跳过
所以最大的集合长度为5,不过这里得输出集合的具体表示,那么我们再用一个数组parent来记录路径即可
注意判断几个特殊情况
1.当数组长度<=1时,直接返回原数组即可
2.当数组中两两都不是倍数的时候,那么还是有答案的,答案随便从数组中取一个数即可
'''

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nlen = len(nums)

        if nlen <= 1:
            return nums
        nums.sort()

        dp = [0]*(nlen+1)
        parent = [0]*(nlen+1)

        mmax, mmaxi = 0, 0  # mmax为当前最大的集合长度, mmaxi代表这个集合中的最后一个数

        for i in range(nlen):
            dp[i] = 1
            for j in range(0, i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1: # 满足条件
                    dp[i] = dp[j] + 1
                    parent[i] = j   # 记录当前最长的路径

                    if dp[i] > mmax:    # 最大值
                        mmax = dp[i]
                        mmaxi = i   # 记录最大值的下标

        if mmax == 0:
            return [nums[0]]

        res = []
        for i in range(mmax):
            res.append(nums[mmaxi]) #
            mmaxi = parent[mmaxi]   # 往上找转移的节点

        return res

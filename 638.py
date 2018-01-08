# coding:utf-8

# 638. Shopping Offers

# https://leetcode.com/problems/shopping-offers/description/


'''
记忆化搜索
参数是当前还要得到的物品个数列表,我们也以此为记忆化的key
对于当前的物品个数列表,首先计算出它不使用优惠时候的价格
然后开始遍历那些special offset
对于每个符合条件的special offser我们开始递归求解它的最小值,然后将其保存在以当前物品列表为key的map中
'''

class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        d = {}
        nlen = len(needs)

        def dfs(cur):
            val = sum([cur[i]*price[i] for i in range(nlen)])
            for spec in special:
                tmp = [cur[i]-spec[i] for i in range(nlen)]
                if min(tmp) < 0:
                    continue
                val = min(val, d.get(tuple(cur), dfs(tmp)) + spec[-1])

            d[tuple(cur)] = val
            return val

        return dfs(needs)
# coding:utf-8


# 135. Candy

# https://leetcode.com/problems/candy/description/


'''
这道题目也挺不错的,没有复杂的算法,想法比较巧妙.好像以前做过类似的题目
要维持题目说的每个人至少一个糖果,high rating的人要比隔壁的得到更多的糖果
那么其实两遍循环就行了,初始的时候每个人都只有一个糖果
第一遍从头到尾, 要是后面的比前面的rating大,那么后面的人得到的糖果数等于前面人糖果数+1,这样满足了右边high rating get more candies
第二遍从尾到头, 要是前面的比后面的rating大,注意此时还需要照顾到已经维护好关系的糖果数目,
在 后面的人糖果数+1 和 前面人本身已经有的糖果数 之中取更大的,来满足左边high rating get more candies的同时维护右边已经
得到的糖果数
这样最后求和即可!
'''


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        rlen = len(ratings)
        res = [1] * rlen

        for i in range(1, rlen):
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1

        for i in range(rlen-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                res[i] = max(res[i], res[i+1]+1)

        return sum(res)



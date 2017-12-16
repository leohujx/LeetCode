# coding:utf-8

# 60. Permutation Sequence

# https://leetcode.com/problems/permutation-sequence/description/

'''
康拓展开式(http://blog.csdn.net/lttree/article/details/24798653)
介绍:当给定一个n和某个数字,要求这个数字是第几大的时候
比如n=4, 给定数字2143,那么
在2后面且比2小的数字有1个,那么 1*3!
在1后面且比1小的数字有0个,那么0*2!
在4后面且比4小的数字有1个,那么1*1!
将上述的和相加为7,那么2143就是[1,2,3,4]组合数中第7大的数字.

反过来说,当给定一个n和k时,求n个数字组合中第k大的数字,那么
比如n=4, k=19
首先 k = k-1 = 18(因为排序是从第0开始的,所以18的下标就是第19大的数字)

18 % 3! = 3 --- 0(得3余0,将余数传递下去)
0 % 2! = 0 ---- 0 (得0余0,将余数传递下去)
0 % 1! = 0 --- 0 (得0余0,结束)

那么对于得3余0来说,就是比最左边的数小的有3个,那么这个数字就是4
对于得0余0来说,比左边第二个数字小的有0个,那么这个数字就是1
对于得0余0来说,比左边第三个数字小的有0个,那么这个数字就是2
剩下的还有3
所以在[1,2,3,4]组合数字中第19大的数字为4123
'''

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fac = map(lambda i:reduce(lambda x,y:x*y, [j for j in range(1,i+1)]), [i for i in range(1,10)])
        fac = [1] + fac # [0!, 1!, 2!, 3!...]

        k -= 1

        vis = [0]*10

        res = ""
        for i in range(n):
            div = k/fac[n-i-1]
            mod = k%fac[n-i-1]
            for j in range(1,n+1): # 寻找第div大的
                if vis[j] == 0:
                    if div == 0:
                        break
                    div -= 1

            res += str(j)
            vis[j] = 1
            k = mod

        return res

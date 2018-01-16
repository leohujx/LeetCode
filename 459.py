# coding:utf-8

# 459. Repeated Substring Pattern

# https://leetcode.com/problems/repeated-substring-pattern/description/


'''
这道题目有很巧妙的方法,第一种是我的做法,比较笨
就是将字符串的长度进行因子分解,如果能整除的话就将这个长度当做一个循环节来看待
再比较以该循环节为循环形成的字符串和原字符串是否一致
'''

import math
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        slen = len(s)

        if slen <= 1:
            return False

        f = s[0]
        if f*slen == s:
            return True

        q = int(math.sqrt(slen)) + 1

        for i in range(2, q):
            if slen % i:
                continue
            rep = slen/i # 能够整除
            s1 = s[:i]*rep # 形成的第一个字符串
            s2 = s[:rep]*i  # 形成的第二个字符串
            if s1 == s or s2 == s:
                return True

        return False



'''
第二种方法就巧了去了..
一行代码就行
其实原理也不难,我们举个例子
比如原字符串为
s = SpSp (Sp是一个循环节,并不代表真实的字符串Sp, 对于s来说,至少是有2个Sp的)
那么 2*s = SpSpSpSp
再去掉头部字符和尾部字符[1:-1],假设我们的Sp去掉头部字符以后变为Sx, Sp去掉尾部字符以后变为Sy
那么 (2*s)[1:-1] = SxSpSpsy
所以如果s是循环节形成的,那么s一定在(2*s)[1:-1]中!!
'''

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in (2*s)[1:-1]
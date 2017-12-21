# coding:utf-8

# 28. Implement strStr()

# https://leetcode.com/problems/implement-strstr/description/

'''
复习下KMP算法
当然可以直接用str1.find(str2)来返回答案
'''

class Solution(object):
    def getNext(self, needle):
        nlen = len(needle)
        _next = [0] * (nlen+1)
        _next[0] = -1
        k = -1

        i = 1
        while i < nlen:
            while k > -1 and needle[k+1] != needle[i]: # 不匹配的时候进行回溯
                k = _next[k]

            if needle[k+1] == needle[i]: # 前缀和后缀相同
                k = k+1  # 前后缀相同长度加一

            _next[i] = k    # 记录此时的长度
            i += 1

        return _next

    def kmp(self, haystack, needle):

        k = -1
        i = 0
        hlen = len(haystack)
        nlen = len(needle)

        _next = self.getNext(needle)
        # print _next

        while i<hlen:
            while k > -1 and needle[k+1] != haystack[i]:
                k = _next[k]

            if needle[k+1] == haystack[i]:
                k = k+1

            if k == nlen-1:
                return i - nlen+1

            i += 1

        return -1
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # return haystack.find(needle)
        hlen = len(haystack)
        nlen = len(needle)

        if hlen < nlen:
            return -1
        if nlen == 0:
            return 0

        return self.kmp(haystack, needle)


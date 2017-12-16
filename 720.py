# coding:utf-8

# 720. Longest Word in Dictionary

# https://leetcode.com/problems/longest-word-in-dictionary/description/


'''
把单词扔到一个set中进行排序,然后对于每一个单词,枚举它的前缀,看前缀是否存在于这个set中
'''

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words = set(words)  # 有序集合

        res = ''
        for word in words:
            if (len(word) < len(res)) or (len(word) == len(res) and word >= res):
                continue

            p = ''
            for i in range(len(word)-1):
                p += word[i]
                if p not in words:
                    break
            else:
                res = word

        return res
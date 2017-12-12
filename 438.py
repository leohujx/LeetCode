# coding:utf-8

# 438. Find All Anagrams in a String


# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

'''
这里我利用了mp作为一个字符出现的字典,key为字母,value为字母出现的次数
然后框定p字符串长度这么一个窗口,边移动边判断是否p的全部字母出现在了s的窗口中
'''


class Solution(object):
    def check(self, mp):
        for value in mp.values():
            if value != 0:
                return False
        return True
    def findAnagrams(self, s, p):
        slen = len(s)
        plen = len(p)

        if slen < plen:
            return []

        mp = {}
        for x in p:
            mp[x] = mp.get(x,0) + 1

        res = []
        pplen = plen
        for i in range(plen):
            if s[i] in mp:
                mp[s[i]] -= 1

        if self.check(mp) is True:
            res.append(0)

        for i in range(plen,slen):
            tp = s[i-plen]
            if tp in mp:      # 加上从窗口最左边跑出的字母
                mp[tp] += 1
                pplen += 1
            if s[i] in mp:    # 减去刚进窗口的那个字母的次数
                mp[s[i]] -= 1

            if self.check(mp) is True:
                res.append(i-plen+1)

        return res


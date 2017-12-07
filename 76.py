# coding:utf-8

# 76. Minimum Window Substring

# https://leetcode.com/problems/minimum-window-substring/description/

'''
思路:好题啊好题,
这种类型的题目都可以用以下的思路解决,具体看注释
'''

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 当s的长度小于t或者t长度为0时,那么就返回""
        if len(s) < len(t) or len(t) == 0:
            return ""

        vis = [0]*180
        for cr in t:    # 统计t中每个字符出现的次数
            vis[ord(cr)] += 1

        tsize = len(t)
        # start是窗口的起始位置,end是窗口的终止位置, count是判断t是否完整出现在s中(when count == 0)
        # minStart是最小窗口的起始位置,minLen是最小窗口的长度
        start,end,count, minStart, minLen = 0, 0, tsize, 0, 0x7fffffff

        for cr in s:
            if vis[ord(cr)] > 0:    # 当t中字符出现在s
                count -= 1

            #fk 注意这个是在if外面,即无论cr是否出现在s中,都得减一,所以如果某个字符在t中不存在,那么vis[cr]<0
            vis[ord(cr)] -= 1
            end += 1    # 窗口终止位置+1

            while count == 0:   # 如果这个窗口是个有效窗口(即t完整的出现在了s中)
                if end - start < minLen:    # 如果窗口大小小于最小值,那么记录这个窗口的起始位置和最小的长度
                    minLen = end - start
                    minStart = start
                # 往后面找更小的窗口!!即将窗口start的位置+1, 也就是我从这个窗口中舍弃了这个字符,往后继续找这个字符
                vis[ord(s[start])] += 1
                # 当然这个字符如果是t中存在的(因为如果t中不存在,那么vis[s[start]]+1最大为0,#fk处已经说明),那么舍弃这个字符
                # 跳出该循环,继续往后找这个字符来 -1
                # 当然如果这个字符不在t中存在,那么count仍然为0,while条件仍然成立,说明这个窗口大小可以立即减一
                if vis[ord(s[start])] > 0:
                    count += 1

                # 窗口起始位置往后移动
                start += 1

        return "" if minLen == 0x7fffffff else s[minStart:minStart+minLen]

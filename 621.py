# coding:utf-8

# 621. Task Scheduler

# https://leetcode.com/problems/task-scheduler/description/


'''
思路: 将所有任务出现的次数统计一遍,按照任务个数从大到小进行执行,刚开始我就是这么做的,但是这么做有问题
比如 [A,A,A,A,A,A,B,C,D] n=2
按照原来思路那么执行顺序就是 A B C D A null null A null null A null null A null null A(17)
其实更好的顺序是 A B C A D null A null null A null null A null null A(16)
所以确切的思路是
先按照出现次数从大到小排序,然后将n视作一个周期,在这个周期内尽可能放上不同的任务,否则就空闲,
然后在下一个周期重新将任务出现的次数排序,重新做上述的循环,直到所有任务被安排完毕
'''


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        num = [0]*26
        total = len(tasks)
        for task in tasks:
            num[ord(task) - ord('A')] += 1
        num.sort(reverse=True)  # 从大到小排序
        interval = 0
        while num[0] > 0:   # 还存在任务
            i = 0
            while i <= n:   # 一个周期
                if num[0] == 0: # 不存在任务的话就跳出循环
                    break
                if i < 26 and num[i] > 0: # 安排任务
                    num[i] -= 1
                interval += 1   # 如果没有任务安排了,那么只有这个语句和下个语句会被一直执行
                i += 1          # 循环下一个出现次数最大的任务
            num.sort(reverse=True)
        return interval
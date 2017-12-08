# coding:utf-8

# 690. Employee Importance

# https://leetcode.com/problems/employee-importance/description/

'''
水题,不过用dfs会更简便
'''

"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        mp = {}
        for (i,employee) in enumerate(employees):
            mp[employee.id] = employee

        if id not in mp:
            return 0

        ans = 0

        myself = mp[id]
        ans += myself.importance

        subList = []
        for sub in myself.subordinates:
            subList.append(sub)

        while len(subList) > 0:
            id = subList.pop()
            idList = mp[id]
            ans += idList.importance
            subList.extend(idList.subordinates)

        return ans


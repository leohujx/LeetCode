# coding:utf-8


# 678. Valid Parenthesis String

# https://leetcode.com/problems/valid-parenthesis-string/description/


'''
这道题目比较麻烦的就是怎么处理*
*既可以当(也可以当)
所以怎么确定某个*可以当什么符号
其实这个可以不用关注具体的,只要对整体进行处理即可
这道题目的解法可以说很巧妙了
我们关注左括号的个数,对于某个字符就是左括号,那么不用说,肯定算一个,如果是*号的话,既可以做左括号,又可作右括号
所以我们来维护下左括号个数的一个区间[mminLeftBracket, mmaxLeftBracket]
何谓最小的个数,那就是将(当做左括号,将)和*都当做是右括号
何谓是最大的个数,那就是将(和*都当做左括号,)当做右括号
那么怎么依据这两个值来进行字符串合法性的判断呢?
首先最大个数肯定是大于0的,如果有小于0的情况,那么肯定不合法,说明)太多了
那么如果左括号太多怎么办呢?那就根据最小个数来判断,如果到最后最小的个数不为0,说明(太多了,
不过还有注意的一点事我们需要在维护的过程中始终保证mminLeftBracket的值是大于等于0的,因为它确实有可能小于0
比如 (**)这样的,其实到第三个字符它已经小于0了,但是其实也还是合法的,因为*也可以当做空字符串,那么比如())的情况呢?这个
不用担心,这种情况已经归属到最大个数小于0的范围了.
'''
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # ls = s.count("(")
        # rs = s.count(")")

        lo, hi = 0, 0
        for char in s:
            lo += (1 if char == '(' else -1)
            hi += (1 if char !=')' else -1)
            if hi < 0:
                return False
            lo = max(lo, 0)

        return lo == 0
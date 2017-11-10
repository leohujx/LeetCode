# coding:utf-8

# 331. Verify Preorder Serialization of a Binary Tree


'''
https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/
'''

'''
思路:给定比如树序列 "9,3,4,#,#,1,#,#,2,#,6,#,#"
可以用栈来做,对于数字来说,比如9,那么入栈时为(9,2),2是当前它还剩余的度
模拟几个数字的出栈过程(遍历序列):
(9,2)
(3,2)
(4,2)
# --> (4,1)
# -->(4,0) --> 4出栈
(3,2) --> (3,1)
(1,2)
# --> (1,1)
# --> (1,0) --> 1出栈
(3,1) --> (3,0) --> 3出栈
(9,2) --> (9,1)......
'''

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        seq = preorder.split(",")
        seq_len = len(seq)
        if seq_len & 1 == 0:    # 必须为奇数个点
            return False

        if seq[0] == '#' and seq_len == 1:  # note the empty tree!
            return True

        tree_list = []
        sindex = 0
        while 1:
            while tree_list and sindex < seq_len and seq[sindex] == '#':
                tree_list[len(tree_list)-1][1] -= 1 # 减一
                while tree_list and tree_list[len(tree_list)-1][1] <= 0:
                    tree_list.pop() # 出栈
                    if not tree_list:
                        break
                    tree_list[len(tree_list)-1][1] -= 1 # 减一
                sindex += 1
            if sindex >= seq_len:
                break

            if seq[sindex] == '#':  # note the illegal tree such as '#,#,#'
                return False

            tree_list.append([seq[sindex], 2])
            sindex += 1
            if sindex >= seq_len:
                break

        return not tree_list
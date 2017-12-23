# coding:utf-8

# 648. Replace Words

# https://leetcode.com/problems/replace-words/description/


'''
python字典树模板
'''

class dTree(object):
    def __init__(self, val):
        self.val = val
        self.charset = {}
        self.isAword = 0
        pass

def converTonum(char):
    return ord(char) - ord('a')

class Solution(object):
    def createTree(self, item, root):
        cur = root
        for char in item:
            if char not in cur.charset:
                newdtree = dTree(char)
                cur.charset[char] = newdtree
                cur = cur.charset[char]
            else:
                cur = cur.charset[char]

        cur.isAword = 1

    def replaceWork(self,sentence, root):
        cur = root
        nr = ""
        res = ""
        for char in sentence:
            if char not in cur.charset:
                if cur.isAword == 1:
                    res = nr
                else:
                    res = sentence
                break
            else:
                cur = cur.charset[char]
                nr += char
                if cur.isAword == 1:
                    res = nr
                    break
        # 注意当res为空的时候,说明这个sentence是字典树中一个单词的前缀,所以一直没有到res的赋值语句
        # 所以当res为空的时候,res应该就等于这个单词
        if res == "":
            res = sentence
        return res

    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        root = dTree('')
        for item in dict:
            self.createTree(item, root)

        sentences = sentence.split()
        newSentence = []
        for sentence in sentences:
            newSentence.append(self.replaceWork(sentence, root))
        # newSentence = self.replaceWork(sentence, root)

        return " ".join(newSentence)

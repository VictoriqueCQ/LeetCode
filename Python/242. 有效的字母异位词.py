class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t) 

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        for char in t:
            if char in count:
                count[char] -= 1
            else:
                return False
        for value in count.values():
            if value != 0:
                return False
        return True


        ###用传统循环方法进行排序比较
        '''
        if len(s) != len(t):
            return False
        s = list(s)
        s.sort()
        t = list(t)
        t.sort()
        for i in range(len(s)):
            if s[i] == t[i]:
                continue
            else:
                return False
        return True
        '''
        #remove方法在数组长度相等的情况下查看删除字符后是否全删完，这里用异常的方式ValueError 搜索列表中不存在
        '''if len(s) != len(t):
            return False
        s = list(s)
        t = list(t)
        for i in s:
            try:
                t.remove(i)
            except ValueError as e:
                return False
        return True'''
        #用哈希索引的方法去比较建立字典
        if len(s) != len(t):
            return False
        words = [chr(i) for i in range(97,123)]
        value = [0]*26
        wordDict_s = dict(zip(words,value))
        wordDict_t = dict(zip(words,value))
        for word in s:
            wordDict_s[word] += 1
        for word in t:
            wordDict_t[word] += 1
        if wordDict_s == wordDict_t:
            return True
        return False

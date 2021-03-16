#
# longest common substring
# @param str1 string字符串 the string
# @param str2 string字符串 the string
# @return string字符串
#
class Solution:
    def LCS(self , str1 , str2 ):
        # write code here
        if len(str1)<len(str2):
            str1,str2 = str2,str1
        res = ""
        max_len = 0
        for i in range(0,len(str1)):
            if str1[i-max_len:i+1] in str2:
                res = str1[i-max_len:i+1]
                max_len+=1
        return res
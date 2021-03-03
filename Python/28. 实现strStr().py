# Implement strStr().
#
# Returns the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        size1 = len(haystack)
        size2 = len(needle)
        if size2 == 0:
            return 0
        if size1 < size2:
            return -1
        i = 0
        while i < size1:
            if size1 - i < size2:
                return -1
            if haystack[i] == needle[0]:
                j = 1
                while j < size2:
                    if haystack[i + j] != needle[j]:
                        break
                    j += 1
                if j == size2:
                    return i
            i += 1
        return -1

    #或者直接return haystack.find(needle)


class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        len1 = len(haystack)
        len2 = len(needle)
        for i in range(len1-len2+1):
            if haystack[i:i+len2] == needle:
                return i
        return -1

#
#
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxLength(self , arr ):
        # write code here
        longest = 0
        cur_list = []
        for i in arr:
            if i in cur_list:
                longest = max(longest,len(cur_list))
                a = cur_list.index(i)
                cur_list = cur_list[a+1:]
            cur_list.append(i)
        return max(longest,len(cur_list))
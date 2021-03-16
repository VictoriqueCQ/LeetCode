# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None:
            return None
        L,M,R = None, None, pHead
        while R.next != None:
            L = M
            M = R
            R = R.next
            M.next = L
        R.next = M
        return R
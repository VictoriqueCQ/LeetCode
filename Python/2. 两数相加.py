# You are given two non-empty linked lists representing two non-negative integers.
#  The digits are stored in reverse order and each of their nodes contain a single digit.
#  Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        l1,l2为输入的待加和的两个串
        """

        # 将两个单链表串按位扫到列表listnum1和listnum2中
        ans = ListNode(0)
        tmp = ans
        tmpsum = 0
        while True:
            if l1 != None:
                tmpsum += l1.val
                l1 = l1.next
            if l2 != None:
                tmpsum += l2.val
                l2 = l2.next
            tmp.val = tmpsum % 10
            tmpsum //= 10
            if l1 == None and l2 == None and tmpsum == 0:
                break
            tmp.next = ListNode(0)
            tmp = tmp.next
        return ans

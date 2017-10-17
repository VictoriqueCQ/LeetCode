# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        tmp = ans
        if l1 == None and l2 == None:
            return None
        while l1 != None or l2 != None:
            if l1 == None:
                while l2 != None:
                    tmp.val = l2.val
                    l2 = l2.next
                    if l2 == None:
                        break
                    tmp.next = ListNode(0)
                    tmp = tmp.next
                break
            if l2 == None:
                while l1 != None:
                    tmp.val = l1.val
                    l1 = l1.next
                    if l1 == None:
                        break
                    tmp.next = ListNode(0)
                    tmp = tmp.next
                break
            if l1.val <= l2.val:
                tmp.val = l1.val
                l1 = l1.next
            else:
                tmp.val = l2.val
                l2 = l2.next
            tmp.next = ListNode(0)
            tmp = tmp.next
        return ans

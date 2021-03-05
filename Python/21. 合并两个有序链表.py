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
        # ans = ListNode(0)
        # tmp = ans
        # if l1 == None and l2 == None:
        #     return None
        # while l1 != None or l2 != None:
        #     if l1 == None:
        #         while l2 != None:
        #             tmp.val = l2.val
        #             l2 = l2.next
        #             if l2 == None:
        #                 break
        #             tmp.next = ListNode(0)
        #             tmp = tmp.next
        #         break
        #     if l2 == None:
        #         while l1 != None:
        #             tmp.val = l1.val
        #             l1 = l1.next
        #             if l1 == None:
        #                 break
        #             tmp.next = ListNode(0)
        #             tmp = tmp.next
        #         break
        #     if l1.val <= l2.val:
        #         tmp.val = l1.val
        #         l1 = l1.next
        #     else:
        #         tmp.val = l2.val
        #         l2 = l2.next
        #     tmp.next = ListNode(0)
        #     tmp = tmp.next
        # return ans

        # if l1 and l2:
        #     if l1.val > l2.val: l1, l2 = l2, l1
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        # return l1 or l2
        if not l2:
            return l1
        if not l1:
            return l2
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

class Solution1:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
class Solution2:
    def mergeTwoLists(self, l1, l2):
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2

        return prehead.next

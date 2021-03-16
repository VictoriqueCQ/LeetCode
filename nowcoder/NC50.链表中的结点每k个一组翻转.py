# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param head ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:
    def reverseKGroup(self , head , k ):
        # write code here
        # if not head or not head.next:
        #     return head
        # newHead = head.next
        # head.next = self.swapPairs(newHead.next)
        # newHead.next = head
        # return newHead
        if not head or not head.next: return head
        tail = head
        for i in range(k):
            if not tail:
                return head
            tail = tail.next
        new_head = self.reverse(head,tail)
        head.next = self.reverseKGroup(tail,k)
        return new_head

    def reverse(self,head,tail):
        pre = None
        next = None
        while head != tail:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre
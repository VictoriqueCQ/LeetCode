# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def detectCycle(self , head ):
        # write code here
        slow = head
        fast = head
        flag = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = True
                break
        if not flag:
            return
        else:
            fast = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr, prev = head, None
        while curr:
            prev, curr.next, curr = curr, prev, curr.next
        return prev

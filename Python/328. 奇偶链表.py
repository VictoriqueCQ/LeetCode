# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        odd, even = head, head.next
        firstEven = even
        # 1->2->3->4->5->null
        while even and even.next:
            # 1->3
            odd.next = even.next
            odd = odd.next
            # 2->4
            even.next = odd.next
            even = even.next
        # 5->2
        odd.next = firstEven

        return head

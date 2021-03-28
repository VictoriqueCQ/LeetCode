# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# class Solution:
#     def reverseBetween(self, head, m, n):
#         """
#         :type head: ListNode
#         :type m: int
#         :type n: int
#         :rtype: ListNode
#         """
#
#         # Empty list
#         if not head:
#             return None
#
#         # Move the two pointers until they reach the proper starting point
#         # in the list.
#         cur, prev = head, None
#         while m > 1:
#             prev = cur
#             cur = cur.next
#             m, n = m - 1, n - 1
#
#         # The two pointers that will fix the final connections.
#         tail, con = cur, prev
#
#         # Iteratively reverse the nodes until n becomes 0.
#         while n:
#             third = cur.next
#             cur.next = prev
#             prev = cur
#             cur = third
#             n -= 1
#
#         # Adjust the final connections as explained in the algorithm
#         if con:
#             con.next = prev
#         else:
#             head = prev
#         tail.next = cur
#         return head


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 设置 dummyNode 是这一类问题的一般做法
        # dummy_node = ListNode(-1)
        # dummy_node.next = head
        # pre = dummy_node
        # for _ in range(left - 1):
        #     pre = pre.next
        #
        # cur = pre.next
        # for _ in range(right - left):
        #     # pre,cur.next,cur = cur,pre,cur.next
        #     next,cur.next,next.next,pre.next = cur.next,next.next,pre.next,next
        #     # next = cur.next
        #     # cur.next = next.next
        #     # next.next = pre.next
        #     # pre.next = next
        # return dummy_node.next

        def reverse(head, k):
            pre, cur = None, head
            for _ in range(k):
                pre, cur.next, cur = cur, pre, cur.next
            return pre, head

        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        for _ in range(m - 1):
            pre = pre.next

        cur = pre.next
        tail = pre.next
        for _ in range(n - m + 1):
            tail = tail.next
            # next = cur.next
            # cur.next = next.next
            # next.next = pre.next
            # pre.next = next
        y, x = reverse(cur, n - m + 1)
        x.next = tail
        pre.next = y
        return dummy_node.next
first = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)
fifth = ListNode(5)
first.next = second
second.next = third
third.next = fourth
fourth.next = fifth
s = Solution()
print(s.reverseBetween(first,2,4))

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    #     dummy = ListNode(0)
    #     dummy.next = head
    #
    #     pre, end = dummy, dummy
    #
    #     while end.next:
    #         # 取出待翻转的部分
    #         i = 0
    #         while i < k and end:
    #             end = end.next
    #             i += 1
    #         if not end: break
    #
    #         # 断开链表
    #         startNode = pre.next
    #         nextNode = end.next
    #         end.next = None
    #
    #         # 处理翻转
    #         pre.next = self.reverse(startNode)
    #         # startNode 转到翻转这部分节点的最后了
    #
    #         # 连接断开的链表
    #         startNode.next = nextNode
    #
    #         # 挪动以进行下一组处理
    #         pre = startNode
    #         end = pre
    #     return dummy.next
    #
    # def reverse(self, head):
    #     pre = None
    #     curr = head
    #     while curr:
    #         nextNode = curr.next
    #         curr.next = pre
    #         pre = curr
    #         curr = nextNode
    #     return pre
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
#     cur = head
#     for _ in range(k):
#         if not cur:
#             return head
#         cur = cur.next
#
#     pre, cur = None, head
#     for _ in range(k):
#         cur.next, pre, cur = pre, cur, cur.next
#
#     head.next = self.reverseKGroup(cur, k)
#     return pre


    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    # 反转 k 个元素，返回反转后的头、尾节点。
        def revrese(head, k):
            pre, cur = None, head
            for _ in range(k):
                cur.next, pre, cur = pre, cur, cur.next
            return pre, head

        pre = dummy = ListNode(0)
        dummy.next = head

        while pre.next:

        # 判断剩余节点个数是否有 k 个，若没有直接返回。
        # 另一个目的是将 cur 定位到 k+1 个节点的位置，方便后续的拼接。
            cur = pre.next
            for _ in range(k):
                if not cur:
                    return dummy.next
                cur = cur.next

            pre.next, pre = revrese(pre.next, k)  # 将 pre 连接已经反转好的元素，顺便移动 pre 的位置。
            pre.next = cur  # 拼接剩余元素，否则无法继续迭代。

        return dummy.next

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
print(s.reverseKGroup(first,3).val)
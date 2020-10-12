# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head:
            # 快慢指针寻找中间点
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            # 分割链表
            insert = slow.next  # 取出
            slow.next = None  # 截断

            # 后半部分链表翻转
            cur_i, pre = insert, None
            while cur_i:
                tmp = cur_i.next
                cur_i.next = pre
                pre = cur_i
                cur_i = tmp

            # 插入
            insert = pre
            cur1, cur2 = insert, head
            while cur1:
                tmp1 = cur2.next  # 暂存右侧部分
                cur2.next = None  # 截断
                tmp2 = cur1.next  # 暂存右侧部分
                cur1.next = None  # 截断
                cur2.next = cur1  # 插入
                cur2.next.next = tmp1  # 拼接
                cur1 = tmp2  # 恢复
                cur2 = cur2.next.next  # 滑动

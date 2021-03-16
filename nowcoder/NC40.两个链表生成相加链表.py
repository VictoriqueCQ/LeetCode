class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
#
# @param head1 ListNode类
# @param head2 ListNode类
# @return ListNode类
#
class Solution:
    def addInList(self, head1, head2):
        # write code here
        def reverse(head):
            cur = head
            pre = None
            nxt = None
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre

        dummy = ListNode(-1)
        p = dummy
        head1 = reverse(head1)
        head2 = reverse(head2)
        flag = 0
        while head1 or head2:
            temp = flag
            if head1:
                temp += head1.val
                head1 = head1.next
            if head2:
                temp += head2.val
                head2 = head2.next
            if temp >= 10:
                temp = temp % 10
                flag = 1
            else:
                flag = 0
            node = ListNode(temp)
            print(temp)
            p.next = node
            p = p.next
        if flag:
            node = ListNode(1)
            p.next = node
        return reverse(dummy.next)








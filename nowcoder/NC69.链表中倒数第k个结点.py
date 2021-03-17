# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:
    def FindKthToTail(self , pHead , k ):
        # write code here
        if not pHead or k <= 0:return None
        node1 = pHead
        node2 = pHead
        for i in range(k-1):
            if node1.next:
                node1 = node1.next
            else:
                return None
        while node1.next:
            node1 = node1.next
            node2 = node2.next
        return node2
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param head ListNode类
# @return bool布尔型
#
class Solution:
    def hasCycle(self , head ):
        # write code here
        node_list = []
        flag = False
        p = head
        while p != None:
            if p in node_list:
                flag = True
                break
            node_list.append(p)
            p = p.next
        return flag


class Solution:
    def hasCycle(self, head):
        p1 = head
        p2 = head
        while p1 != None:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
            else:
                return False

        # write code here
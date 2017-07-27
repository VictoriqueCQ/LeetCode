# You are given two non-empty linked lists representing two non-negative integers.
#  The digits are stored in reverse order and each of their nodes contain a single digit.
#  Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        l1,l2为输入的待加和的两个串
        """

        # 将两个单链表串按位扫到列表listnum1和listnum2中
        listnum1 = []
        listnum2 = []
        while l1 != None:
            listnum1.append(l1.val)
            l1 = l1.next
        while l2 != None:
            listnum2.append(l2.val)
            l2 = l2.next

            # 将两个数用整型num1和num2表示出来（**运算为指数运算，eg. 2 ** 3 结果为8）
        num1 = 0
        num2 = 0
        for i in range(len(listnum1)):
            num1 = listnum1[i] * (10 ** i) + num1
        for j in range(len(listnum2)):
            num2 = listnum2[j] * (10 ** j) + num2

            # 计算结果后，构造结果的单链表结构l3
        result = num1 + num2
        l3 = ListNode(0)
        p = ListNode(0)
        p = l3
        # l3和p指向首节点，构造过程中l3不动，仍指向首节点，p进行构造移动
        while result >= 10:
            temp = ListNode(None)
            p.val = result % 10
            p.next = temp
            p = temp
            result = result / 10
            # 由于循环到最后一个节点时不再构造新节点，于是退出循环，并给最后一个节点赋值
        p.val = result % 10
        return l3

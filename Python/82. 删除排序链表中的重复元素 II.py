class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = pre = ListNode(0)
        dummy.next = head            # 根据上式的赋值,改变dummy的结构也会改变pre
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next # 向后移动head指针
                head = head.next     # 继续后移以去除重复出现过的数字
                pre.next = head      # 此时head指向中间位置所代表的后序链表,通过pre指针将前序排序连接上,
                # 此处对pre的操作破坏了链表的结构,由于dummy与pre指向同一链表,所以return dummy的值会发生变化(去重),
                # 但dummy仍旧指向链表的开头ListNode(0)所以可以return到一开始的元素如0->1->2->3->3->4有
                # 0->1->2->4,而pre为2->4
            else:
                head = head.next
                pre = pre.next
        return dummy.next # 如果输出pre.next的话 拿预期[1,2,5]的输出为例 只能得到[5]


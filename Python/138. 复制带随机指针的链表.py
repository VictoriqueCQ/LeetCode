# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        lookup = {}
        def dfs(head):
            if not head: return None
            if head in lookup: return lookup[head]
            clone = Node(head.val, None, None)
            lookup[head] = clone
            clone.next, clone.random = dfs(head.next), dfs(head.random)
            return clone
        return dfs(head)


class Solution2:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # 第一遍遍历，把每个新生成的结点放在对应的旧结点后面
        p = head
        while p:
            new_node = Node(p.val)
            new_node.next = p.next
            p.next = new_node

            p = new_node.next  # 下一个旧结点

        # 第二遍修改每个新结点的 next 和 random
        p = head
        while p:
            next_origin = p.next.next  # 下一个旧结点备份一下
            p.next.next = next_origin.next if next_origin else None  # 修改新结点的 next
            p.next.random = p.random.next if p.random else None  # 修改新结点的 random

            p = next_origin  # 下一个旧结点

        return head.next



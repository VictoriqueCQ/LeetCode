
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        leftmost = root

        while leftmost:

            dummy = Node(0)
            tail = dummy

            while leftmost:
                if leftmost.left:
                    tail.next = leftmost.left
                    tail = tail.next

                if leftmost.right:
                    tail.next = leftmost.right
                    tail = tail.next

                leftmost = leftmost.next

            leftmost = dummy.next
        return root
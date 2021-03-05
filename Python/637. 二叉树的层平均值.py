# Definition for a binary tree node.
import collections
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        def dfs(root: TreeNode, level: int):
            if not root:
                return
            if level < len(totals):
                totals[level] += root.val
                counts[level] += 1
            else:
                totals.append(root.val)
                counts.append(1)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        counts = list()
        totals = list()
        dfs(root, 0)
        return [total / count for total, count in zip(totals, counts)]

class Solution1:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        averages = list()
        queue = collections.deque([root])
        while queue:
            total = 0
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                total += node.val
                left, right = node.left, node.right
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
            averages.append(total / size)
        return averages

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s = Solution1()
print(s.averageOfLevels(root))
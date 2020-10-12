# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root):
        nodes, values, step = [(root,)], [], 1
        while nodes:
            values.append([r.val for n in nodes[::step] for r in n[::step] if r])
            step, nodes = -step, [(r.left, r.right) for n in nodes for r in n if r]
        return values[:-1]

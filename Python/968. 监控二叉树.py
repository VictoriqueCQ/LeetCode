# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lrd(self, node: TreeNode) -> int:
        global res
        res = 0
        if node == None:
            return 1
        left = self.lrd(node.left)
        right = self.lrd(node.right)
        if left == 0 or right == 0:
            res += 1
            return 2
        if left == 1 and right == 1:
            return 0
        if left + right >= 3:
            return 1
        return -1

    def minCameraCover(self, root: TreeNode) -> int:
        global res
        if self.lrd(root) == 0:
            res += 1
        return res

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.cameras = 0
        self.dfs_greedy(root)
        return self.cameras + int(root.val == 1)
    def dfs_greedy(self, root):
        if not root:
            return 0
        left = self.dfs_greedy(root.left)
        right = self.dfs_greedy(root.right)
        if left == 0 and right == 0:
            root.val = 1
        elif left == 1 or right == 1:
            root.val = 2
            self.cameras = self.cameras + 1
        else: #left == 2 or right == 2:
            root.val = 0
        return root.val
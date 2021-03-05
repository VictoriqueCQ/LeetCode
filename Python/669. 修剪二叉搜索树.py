# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def trim(node):
            if not node:
                return None
            elif node.val > high:
                return trim(node.left)
            elif node.val < low:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:

        def dfs(root, L, R):
            if root is None:
                return
            if root.val > R:
                root = dfs(root.left, L, R)
            elif root.val < L:
                root = dfs(root.right, L, R)
            else:
                root.left = dfs(root.left, L, R)
                root.right = dfs(root.right, L, R)
            return root

        return dfs(root, L, R)


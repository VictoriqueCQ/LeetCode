# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def dfs(inorder, in_start, in_end, postorder, post_start, post_end):
            if in_start > in_end: return None
            if in_start == in_end: return TreeNode(inorder[in_start])
            if post_start == post_end: return TreeNode(inorder[in_start])
            root = TreeNode(postorder[post_end])
            i = inorder.index(root.val)
            root.left = dfs(inorder, in_start, i - 1, postorder, post_start, post_start + i - 1 - in_start)
            root.right = dfs(inorder, i + 1, in_end, postorder, post_start + i - 1 - in_start + 1, post_end - 1)
            return root
        n = len(inorder)
        return dfs(inorder, 0, n - 1, postorder, 0, n - 1)
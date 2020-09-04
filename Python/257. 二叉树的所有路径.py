# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        q = [[root, []], ]
        res = []

        while q:
            node, tree_link = q.pop(0)
            tree_link = tree_link + [str(node.val)]

            if node.left:
                q.append([node.left, tree_link])
            if node.right:
                q.append([node.right, tree_link])

            if not node.left and not node.right:
                res.append('->'.join(tree_link))

        return res

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        return [] if not root else [str(root.val)] if not root.left and not root.right else [str(root.val)+"->"+i for i in self.binaryTreePaths(root.left)+self.binaryTreePaths(root.right)]



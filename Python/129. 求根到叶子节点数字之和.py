# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    tmp = lambda self, root: [] if not root else [root.val] if not root.left and not root.right \
        else [str(root.val) + str(i) for i in self.tmp(root.left) + self.tmp(root.right)]
    sumNumbers = lambda self, root: sum(map(int, self.tmp(root)))

class Solution1:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        stack = [(root,str(root.val))]
        res = 0
        while stack:
            node,sum = stack.pop(0)
            if node.left:
                stack.append((node.left,sum+str(node.left.val)))
            if node.right:
                stack.append((node.right,sum+str(node.right.val)))
            if not node.left and not node.right:
                res += int(sum)
        return res
class Solution2:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        self.sum = 0
        def dfs(node,sum):
            if node.left:
                dfs(node.left,sum+str(node.left.val))
            if node.right:
                dfs(node.right,sum+str(node.right.val))
            if not node.left and not node.right:
                self.sum += int(sum)
        dfs(root,str(root.val))
        return self.sum


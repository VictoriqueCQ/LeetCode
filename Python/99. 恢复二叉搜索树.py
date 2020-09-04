# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        pre = None  ##利用pre记录中序遍历过程中遍历当前节点的上一个节点
        x = None
        y = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ###此次是找出两个错位的节点逻辑
            if pre and pre.val > root.val:
                y = root
                if x == None:
                    x = pre
            pre = root
            root = root.right
        x.val,y.val = y.val,x.val
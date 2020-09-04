# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        '''
        叶子节点的定义是左孩子和右孩子都为 null 时叫做叶子节点
        1. 当 root 节点左右孩子都为空时，返回 1
        2. 当 root 节点左右孩子有一个为空时，返回不为空的孩子节点的深度
        3. 当 root 节点左右孩子都不为空时，返回左右孩子较小深度的节点值
        '''
        if not root:
            return 0

        left_min = self.minDepth(root.left)
        right_min = self.minDepth(root.right)

        if not root.left and not root.right:  # 情况 1
            return 1
        elif not root.left or not root.right:  # 情况 2
            return left_min + 1 if root.left else right_min + 1
        else:  # 情况 3
            return min(left_min, right_min) + 1
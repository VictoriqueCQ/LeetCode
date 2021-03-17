# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param root TreeNode类 the root
# @return bool布尔型一维数组
#
class Solution:
    def judgeIt(self, root):
        # write code here
        left, right = -float('inf'), float('inf')
        return [self.isSearch(root, left, right), self.isComplete(root)]

    def isSearch(self, root, left, right):
        if not root: return True
        if root.val < left or root.val > right:
            return False
        return self.isSearch(root.left, left, root.val) and self.isSearch(root.right, root.val, right)

    def isComplete(self, root):
        if not root: return True
        if not root.left and not root.right: return True
        if not root.left and root.right: return False
        return self.isComplete(root.left) and self.isComplete(root.right)


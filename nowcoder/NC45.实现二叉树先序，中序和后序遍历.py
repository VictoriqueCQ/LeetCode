# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param root TreeNode类 the root of binary tree
# @return int整型二维数组
#
class Solution:
    def threeOrders(self , root ):
        # write code here
        self.res = [[], [], []]
        self.dfs(root)
        return self.res
    def dfs(self , root ):
        if root is None:
            return False
        self.res[0].append(root.val)
        self.dfs(root.left)
        self.res[1].append(root.val)
        self.dfs(root.right)
        self.res[2].append(root.val)
        return True
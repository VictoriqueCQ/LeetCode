# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param root TreeNode类
# @return int整型二维数组
#
class Solution:
    def levelOrder(self, root):
        # write code here
        if not root: return []
        res = []
        queue = [root]
        while queue:
            subList = []
            for i in range(len(queue)):
                node = queue.pop(0)
                subList.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(subList)
        return res

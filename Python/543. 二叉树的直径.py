# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0
        self.helper(root, diameter)
        return diameter

    def helper(self, node: TreeNode, diameter):
        if not node:
            return 0
        l = self.helper(node.left, diameter)
        r = self.helper(node.right, diameter)
        diameter = max(l + r, diameter)
        return max(l, r) + 1


class Solution1:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1

        def depth(node):
            # 访问到空节点了，返回0
            if not node:
                return 0
            # 左儿子为根的子树的深度
            L = depth(node.left)
            # 右儿子为根的子树的深度
            R = depth(node.right)
            # 计算d_node即L+R+1 并更新ans
            self.ans = max(self.ans, L + R + 1)
            # 返回该节点为根的子树的深度
            return max(L, R) + 1

        depth(root)
        return self.ans - 1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
s = Solution1()
print(s.diameterOfBinaryTree(root))
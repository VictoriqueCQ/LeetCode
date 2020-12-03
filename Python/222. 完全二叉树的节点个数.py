class Solution:
    def countNodes(self, root: TreeNode) -> int:
        rightdepth, left_n, right_n = 0, root, root
        while right_n:
            right_n = right_n.right
            left_n = left_n.left
            rightdepth += 1
        if not left_n:
            return 2**rightdepth-1
        return self.countNodes(root.left)+self.countNodes(root.right)+1

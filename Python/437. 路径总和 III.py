# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 精简版，五行代码不解释
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(root, sumlist):
            if root is None: return 0
            sumlist = [num + root.val for num in sumlist] + [root.val]
            return sumlist.count(sum) + dfs(root.left, sumlist) + dfs(root.right, sumlist)

        return dfs(root, [])


# 展开版，易理解
class Solution1:
    def pathSum(self, root: TreeNode, sum: int) -> int:

        def dfs(root, sumlist):
            if root is None:
                return 0

            sumlist = [num + root.val for num in sumlist]
            sumlist.append(root.val)

            count = 0
            for num in sumlist:
                if num == sum:
                    count += 1
            # count = sumlist.count(sum)

            return count + dfs(root.left, sumlist) + dfs(root.right, sumlist)

        return dfs(root, [])

root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(1)
root.right = TreeNode(-3)
root.right.right = TreeNode(11)
s = Solution1()
print(s.pathSum(root,8))
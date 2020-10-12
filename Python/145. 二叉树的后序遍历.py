# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        l = []
        l.append(root)
        while l:
            node = l[0]
            del l[0]
            result.insert(0, node.val)
            if node.left:
                l.insert(0, node.left)
            if node.right:
                l.insert(0, node.right)
        return result

class Solution2(object):
    def postorderTraversal(self, root):
        res = []  # 用来存储后序遍历节点的值
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)  # 第一次入栈的是根节点
                # 判断当前节点的左子树是否存在，若存在则持续左下行，若不存在就转向右子树
                node = node.left if node.left is not None else node.right
            # 循环结束说明走到了叶子节点，没有左右子树了，该叶子节点即为当前栈顶元素，应该访问了
            node = stack.pop()  # 取出栈顶元素进行访问
            res.append(node.val)  # 将栈顶元素也即当前节点的值添加进res
            # （下面的stack[-1]是执行完上面那句取出栈顶元素后的栈顶元素）
            if stack and stack[-1].left == node:  # 若栈不为空且当前节点是栈顶元素的左节点
                node = stack[-1].right  ## 则转向遍历右节点
            else:
                node = None  # 没有左子树或右子树，强迫退栈
        return res


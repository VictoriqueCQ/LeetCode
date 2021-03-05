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

class Solution1(object):
    def recoverTree(self, root):
        x = None
        y = None
        pre = None
        tmp = None
        while root:
            if root.left:
                tmp = root.left
                while tmp.right and tmp.right!=root:
                    tmp = tmp.right
                if tmp.right is None:
                    tmp.right = root
                    root = root.left
                else:
                    if pre and pre.val>root.val:
                        y = root
                        if not x:
                            x = pre
                    pre = root
                    tmp.right = None
                    root = root.right
            else:
                if pre and pre.val>root.val:
                    y = root
                    if not x:
                        x = pre
                pre = root
                root = root.right
        if x and y:
            x.val,y.val = y.val,x.val

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr=[None,None,None]   #prev,fisrt,second
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if arr[0] and node.val<arr[0].val:
                if not arr[1]:     #第一次出现前一个元素比当前元素大
                    arr[1]=arr[0]  #确定第一元素
                arr[2]=node        #确定第二元素
            arr[0]=node            #prev随遍历向后移动
            dfs(node.right)
        dfs(root)
        arr[1].val,arr[2].val=arr[2].val,arr[1].val

class Solution3(object):
    def recoverTree(self, root):
        nodes = []
        # 中序遍历二叉树，并将遍历的结果保存到list中
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nodes.append(root)
            dfs(root.right)
        dfs(root)
        x = None
        y = None
        pre = nodes[0]
        # 扫面遍历的结果，找出可能存在错误交换的节点x和y
        for i in range(1,len(nodes)):
            if pre.val>nodes[i].val:
                y=nodes[i]
                if not x:
                    x = pre
            pre = nodes[i]
        # 如果x和y不为空，则交换这两个节点值，恢复二叉搜索树
        if x and y:
            x.val,y.val = y.val,x.val

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(2)
s = Solution3()
s.recoverTree(root)
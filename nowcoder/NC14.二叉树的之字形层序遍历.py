class Solution:
    def zigzagLevelOrder(self , root ):
        if not root:return []
        res = []
        queue = [root]
        count = 1
        while queue:
            subList = []
            for i in range(len(queue)):
                node = queue.pop(0)
                subList.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if count%2:
                res.append(subList)
            else:
                res.append(subList[::-1])
            count += 1
        return res
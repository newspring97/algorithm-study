class Solution:
    def pathSumHelper(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        left = self.pathSumHelper(root.left)
        right = self.pathSumHelper(root.right)
        
        res = []
        if len(left) > 0:
            for x in left:
                res.append(x + [root.val])
        if len(right) > 0:
            for y in right:
                res.append(y + [root.val])
        if len(left) == 0 and len(right) == 0:
            res.append([root.val])
        return res
        
            
    
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        tmp = self.pathSumHelper(root)
        res = []
        for route in tmp:
            if sum(route) == targetSum:
                res.append(route[::-1])
        return res
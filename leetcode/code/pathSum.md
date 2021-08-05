# Path Sum

## Path Sum
* [문제 링크](https://leetcode.com/problems/path-sum/)
* 풀이 (2021/08/05)
```python
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def dfs(node, target):
            if node is None:
                return False
            if node.left is None and node.right is None:
                return target == node.val
            return dfs(node.left, target - node.val) or dfs(node.right, target - node.val)
        
        return dfs(root, targetSum)
```

## Path Sum II
* [문제 링크](https://leetcode.com/problems/path-sum-ii/)
* [풀이](../2021AugustChallenge/code/0804.py)

## Path Sum III
* [문제 링크](https://leetcode.com/problems/path-sum-iii/)
* 풀이 (2021/08/05)
    * Time Complexity: O(n^2)
```python
class Solution:
    def pathSumHelper(self, root: TreeNode, targetSum: int) -> (int, List[int]):
        if root is None:
            return 0, []
        left_cnt, left_root = self.pathSumHelper(root.left, targetSum)
        right_cnt, right_root = self.pathSumHelper(root.right, targetSum)
        
        total_cnt = left_cnt + right_cnt
        if root.val == targetSum:
            total_cnt += 1
        res = [root.val]
        for left in left_root:
            if left + root.val == targetSum:
                total_cnt += 1
            res.append(left + root.val)
        for right in right_root:
            if right + root.val == targetSum:
                total_cnt += 1
            res.append(right + root.val)
        return total_cnt, res
    
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        res, _ = self.pathSumHelper(root, targetSum)
        return res
```
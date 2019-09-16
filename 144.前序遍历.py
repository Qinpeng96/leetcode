# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def solve(root):
            if not root:
                return 0;
            res.append(root.val)
            solve(root.left)
            solve(root.right)
        solve(root)
        return res
        
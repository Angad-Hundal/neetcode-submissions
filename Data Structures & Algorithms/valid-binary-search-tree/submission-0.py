class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, left_max, right_min):

            if not root:
                return True

            # Current node must be within the valid range
            if root.val <= left_max or root.val >= right_min:
                return False

            # Left subtree: values must be smaller than root.val
            # Right subtree: values must be larger than root.val
            return (
                dfs(root.left, left_max, root.val)
                and
                dfs(root.right, root.val, right_min)
            )

        return dfs(root, float("-inf"), float("inf"))
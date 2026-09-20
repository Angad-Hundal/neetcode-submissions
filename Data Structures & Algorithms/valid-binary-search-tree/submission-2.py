class Solution:

    # no duplicates
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, left_max, right_min):

            if not root:
                return True

            if root.val <= left_max or root.val >= right_min:
                return False

            return (
                dfs(root.left, left_max, root.val)
                and
                dfs(root.right, root.val, right_min)
            )

        return dfs(root, float("-inf"), float("inf"))
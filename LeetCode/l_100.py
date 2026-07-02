# For every pair of nodes:
# 1. If both are null -> trees match so far.
# 2. If only one is null -> trees are different.
# 3. If values are different -> trees are different.
# 4. Otherwise recursively compare left subtrees and right subtrees.
#
# The trees are the same only if both left and right subtrees are identical.

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
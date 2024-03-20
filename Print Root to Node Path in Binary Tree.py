class Solution:
    def preorder(self, root, result, x):
        if not root:
            return False
        result.append(root.val)
        if root.val == x:
            return True
        if self.preorder(root.left, result, x) or self.preorder(root.right, result, x):
            return True
        result.pop()
        return False
    def rootToPath(self, root, x):
        result = []
        self.preorder(root, result, x)
        return result
        
class Solution:
    # Return the size of the largest sub-tree which is also a BST
    def __init__(self):
        self.max_size = 0
    def postorder(self, root):
        if not root:
            return True, float('inf'), float('-inf'), 0
        left_is_bst, left_min, left_max, left_size = self.postorder(root.left)
        right_is_bst, right_min, right_max, right_size = self.postorder(root.right)
        if left_is_bst and right_is_bst and  left_max <root.data< right_min:
            size = left_size + right_size + 1
            self.max_size = max(self.max_size, size)
            return True, min(left_min, root.data), max(right_max, root.data), size
        return False , 0 , 0 , 0
    def largestBst(self, root):
        #code here
        self.postorder(root)
        return self.max_size
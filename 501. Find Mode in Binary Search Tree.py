# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, freq_map):
        if not root:
            return 
        self.inorder(root.left, freq_map)
        freq_map[root.val] = freq_map.get(root.val, 0)+1
        self.inorder(root.right, freq_map)
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq_map = {}
        self.inorder(root, freq_map)
        max_freq = max(freq_map.values())
        result = [key for key, value in freq_map.items() if value==max_freq]
        return result
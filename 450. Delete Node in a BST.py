# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLastRight(self, node):
        if not node.right:
            return node
        return self.findLastRight(node.right)
    
    def helpher(self, node):
        if not node.left:
            return node.right
        elif not node.right:
            return node.left
        else:
            rightChild = node.right
            lastRight = self.findLastRight(node.left)
            lastRight.right = rightChild
            return node.left

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val == key:
            return self.helpher(root)
        current = root
        while current:
            if current.val > key:
                if current.left and current.left.val == key:
                    current.left = self.helpher(current.left)
                    break
                else:
                    current = current.left
            else:
                if current.right and current.right.val == key:
                    current.right = self.helpher(current.right)
                    break
                else:
                    current = current.right
        return root
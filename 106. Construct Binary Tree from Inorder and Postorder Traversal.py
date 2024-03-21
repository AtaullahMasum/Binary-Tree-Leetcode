# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root_val = postorder.pop()
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)

        root.right = self.buildTree(inorder[root_index+1:], postorder)
        root.left = self.buildTree(inorder[:root_index], postorder)
       
        return root
#using more optimized method
class Solution:
     def buildTreeInPost(self, inorder, inStart, inEnd, postorder, postStart, postEnd):
        # Base case: If there's no elements to construct the subtree
        if inStart > inEnd or postStart > postEnd:
            return None

        # Last element in postorder is the root of the current subtree
        root = TreeNode(postorder[postEnd])
        # Finding the root in inorder to separate left and right subtrees
        inRoot = inorder.index(root.val)
        # Number of nodes in the left subtree
        numLeft = inRoot - inStart

        # Construct left subtree
        root.left = self.buildTreeInPost(inorder, inStart, inRoot - 1, postorder, postStart, postStart + numLeft - 1)
        # Construct right subtree
        root.right = self.buildTreeInPost(inorder, inRoot + 1, inEnd, postorder, postStart + numLeft, postEnd - 1)

        return root
        
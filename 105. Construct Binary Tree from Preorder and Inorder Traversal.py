# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)

        root.left = self.buildTree(preorder, inorder[:root_index])
        root.right = self.buildTree(preorder, inorder[root_index+1:])
        return root
#Using Hashing
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import OrderedDict
class Solution:
    def buildTreePreIn(self, preorder, preStart, preEnd, inorder, inStart, inEnd, ordermap):
        if preStart > preEnd or inStart > inEnd:
            return None
        root = TreeNode(preorder[preStart])
        inRoot = ordermap[root.val]
        numsLeft = inRoot - inStart
        root.left = self.buildTreePreIn(preorder, preStart+1, preStart+numsLeft, inorder, inStart, inRoot-1, ordermap )
        root.right = self.buildTreePreIn(preorder, preStart+numsLeft+1, preEnd, inorder, inRoot+1, inEnd, ordermap)
        return root


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ordermap = OrderedDict()
        for i, value in enumerate(inorder):
            ordermap[value] = i
        for i in range(len(inorder)):
            ordermap[inorder[i]] = i
        root = self.buildTreePreIn(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, ordermap)
        return root
        
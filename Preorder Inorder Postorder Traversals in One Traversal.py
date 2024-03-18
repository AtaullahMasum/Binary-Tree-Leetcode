class TreeNode:
  def __init__(self, val = 0 , left = None, right = None):
    self.val = val
    self.left = left 
    self.right = right
class Solution:
  def PreInPostOrderTraversal(self, root):
    preorder = []
    inorder = []
    postorder = []
    stack = [(root, 1)]
    while stack:
      node , num = stack.pop()
      if num == 1:
        preorder.append(node.val)
        num += 1
        stack.append((node, num))
        if node.left:
          stack.append((node.left, 1))
      elif num == 2:
        inorder.append(node.val)
        num += 1
        stack.append((node, num))
        if node.right:
          stack.append((node.right, 1))
      else:
        postorder.append(node.val)
    return preorder,inorder,postorder

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(3)
root.left.left.right = TreeNode(4)
root.left.left.right.right = TreeNode(5)
root.left.left.right.right.right = TreeNode(6)
root.right.left = TreeNode(6)

ob = Solution()
preorder, inorder, postorder = ob.PreInPostOrderTraversal(root)
print(preorder)
print(inorder)
print(postorder)
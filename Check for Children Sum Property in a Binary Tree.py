
'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
  
    def isLeaf(self, node):
        if not node.left  and not node.right:
            return True
        return False
    def isSumProperty(self, root):
        if not root:
            return 1
        
        # Calculating the sum of children's data.
        children_sum = 0
        if root.left:
            children_sum += root.left.data
        if root.right:
            children_sum += root.right.data
        
        # Checking if the current node's value is equal to the sum of its children's values.
        if  not self.isLeaf(root):
            if root.data != children_sum:
                return 0
        left = self.isSumProperty(root.left)
        right = self.isSumProperty(root.right)
        if not left or not right:
            return 0
        return 1
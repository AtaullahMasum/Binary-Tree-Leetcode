'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    # Return a list containing the preorder traversal of the given tree
    def preOrder(self, root):
        # code here
        result = []
        curr = root
        while curr:
            if not curr.left:
                result.append(curr.data)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if not prev.right:
                    prev.right = curr
                    result.append(curr.data)
                    curr = curr.left
                else:
                    prev.right = None
                    curr = curr.right
        return result


# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

# return the Kth largest element in the given BST rooted at 'root'
class Solution:
    def __init__(self):
        self.count = 0
    def reverseinorder(self, root, k, result):
        if not root:
            return 
        self.reverseinorder(root.right, k, result)
        self.count += 1
        if self.count == k:
            result[0] = root.data
            return
        self.reverseinorder(root.left, k, result)
        
    
    
    def kthLargest(self,root, k):
        #your code here
        result = [0]
        self.reverseinorder(root,k, result)
        return result[0]

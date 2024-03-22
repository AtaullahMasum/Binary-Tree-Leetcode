#Function to return the ceil of given number in BST.
#using iterative way
class Solution:
    def findCeil(self,root, inp):
        # code here
        ceil = -1
        while root:
            if root.key == inp:
                ceil = root.key
                return root.key
            if inp > root.key:
                root = root.right
            else:
                ceil = root.key
                root = root.left
        return ceil
#Using recursively 


class Solution:
    def findCeil(self,root, inp):
        # code here
        if not root:
            return -1
        if root.key == inp:
            return inp
        if inp > root.key:
            return self.findCeil(root.right, inp)
        ceil = self.findCeil(root.left, inp)
        if ceil >= inp:
            return ceil
        return root.key



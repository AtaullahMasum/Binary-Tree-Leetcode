class Solution:
    def floor(self, root, x):
        # Code here
        floor = -1
        while root:
            if root.data == x:
                floor = root.data
                return floor 
            if x > root.data:
                floor = root.data
                root = root.right
            else:
                root = root.left
        return floor
#recursive solution added
class Solution:
    def __init__(self):
        self.floor_value = -1
    def floor(self, root, x):
        # Code here
        if not root:
            return self.floor_value
        if root.data == x:
            return root.data
        if x > root.data:
            self.floor_value = root.data
            return self.floor(root.right, x)
        else:
            return self.floor(root.left, x)
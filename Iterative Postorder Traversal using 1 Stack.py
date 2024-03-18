class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorder(self, root):
        if not root:
            return []

        stack = []
        result = []
        current = root
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                temp = stack[-1].right
                if not temp:
                    temp = stack.pop()
                    result.append(temp.val)
                    while stack and temp == stack[-1].right:
                        temp = stack.pop()
                        result.append(temp.val)
                else:
                    current = temp
        return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(3)
root.left.left.right = TreeNode(4)
root.left.left.right.right = TreeNode(5)
root.left.left.right.right.right = TreeNode(6)
root.right.left = TreeNode(6)

ob = Solution()
print(ob.postorder(root))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def dfs(node):
            if not node:
                return ""
            return str(node.val) + ',' + dfs(node.left) + dfs(node.right)
        
        return dfs(root)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def dfs(min_val, max_val):
            if not nodes or not nodes[0] or not min_val < int(nodes[0]) < max_val:
                return None
            root_val = int(nodes.pop(0))
            root = TreeNode(root_val)
            root.left = dfs(min_val, root_val)
            root.right = dfs(root_val, max_val)
            return root
        
        nodes = data.split(',')
        return dfs(float('-inf'), float('inf'))
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
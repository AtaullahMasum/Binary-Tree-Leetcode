
class Solution:
    def preorder(self, root, max_sum, path_sum, max_path, current_path):
        if not root:
            return
        current_path.append(root.data)
        path_sum += root.data
        if not root.left and not root.right:
            if path_sum > max_sum[0]:
                max_sum[0] = path_sum
                max_path = current_path[:]
        self.preorder(root.left, max_sum, path_sum, max_path, current_path)
        self.preorder(root.right, max_sum, path_sum, max_path, current_path)
        current_path.pop()
        path_sum -= root.data
            
    def maxPathSum(self, root):
        #code here
        max_sum =[float('-inf')]
        max_path = []
        self.preorder(root, max_sum, 0, max_path, [])
        return max_sum[0]
        

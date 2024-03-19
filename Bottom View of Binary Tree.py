from collections import defaultdict
class Solution:
    def bottomView(self, root):
        # code here
        if not root:
            return []
        result = []
        vertical_levels = defaultdict(int)
        queue = [(root, 0)]
        while queue:
            node, vertical_line = queue.pop(0)
            vertical_levels[vertical_line] = node.data
            if node.left:
                queue.append((node.left, vertical_line-1))
            if node.right:
                queue.append((node.right, vertical_line +1))
        for x in sorted(vertical_levels):
            result.append(vertical_levels[x])
        return result

class Solution:
    def dfs(self,node,depth):
        if not node:
            return -1
        if not node.left and not node.right:
            if depth>self.max_depth:
                self.candidate = node 
                self.max_depth = depth
            return depth

        left_depth = self.dfs(node.left,depth+1)
        right_depth = self.dfs(node.right,depth+1)
        if left_depth==right_depth==self.max_depth:
            self.candidate = node
        return max(left_depth,right_depth)

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.candidate = None
        self.max_depth = -1
        self.dfs(root,0)
        return self.candidate

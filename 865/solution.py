from collections import defaultdict
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        di = defaultdict(set)
        deep = [0]
        deepNodes = set()
        def func(node,level):
            nodes = set()
            deep[0] = max(deep[0],level) 
            if node:                
                nodes.add(node)
                if node.left:
                    nodes = nodes | func(node.left,level+1)
                if node.right:
                    nodes = nodes | func(node.right,level+1)
                di[node] = nodes
            return nodes 
            
        head = root
        func(head,1)
        def deepness(node,level):
            if node:
                if level==deep[0]:
                    deepNodes.add(node)
                deepness(node.left,level+1)
                deepness(node.right,level+1)
        head = root
        deepness(head,1)
        
        result = [None]
        def dfs(node):
            if node and not result[0]:
                dfs(node.left)
                dfs(node.right)
                ck = True
                for k in deepNodes:
                    if not k in di[node]:
                        ck = False
                        break
                if ck and not result[0]:
                    result[0] = node
        dfs(root)
        return result[0]

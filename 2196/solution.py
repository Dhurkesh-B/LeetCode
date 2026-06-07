class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        rootNode = set(x for data in descriptions for x in data[:2])
        nodes = {}
        for parent, child, isLeft in descriptions:
            if not parent in nodes:
                nodes[parent] = [None, None]
            nodes[parent][isLeft-1] = child
            rootNode.remove(child)
        def createNodes(node):
            newNode = TreeNode(node)
            if node in nodes:
                if nodes[node][0]:
                    newNode.left = createNodes(nodes[node][0])
                if nodes[node][1]:
                    newNode.right = createNodes(nodes[node][1])
            return newNode
        rootNode, = rootNode
        res = createNodes(rootNode)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        def dfs(node):
            if not node:
                result.append("N")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(result) # "1, N, 2"

    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        val = data.split(',')
        self.i = 0

        def dfs():
            if val[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(str(val[self.i]))
            self.i += 1

            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()


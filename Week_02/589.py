# # Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        self.do(root, res)
        return res

    def do(self, node, res):
        if node is None:
            return

        res.append(node.val)

        for child in node.children:
            self.do(child, res)

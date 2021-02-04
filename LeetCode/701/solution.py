# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
#         if root:
#             node  = root
#             print(root)
#             while (1):
#                 if val >= node.val:
#                     if node.right:
#                         node = node.right
#                         pass
#                     else:
#                         node.right = TreeNode(val)
#                         break
#                 else:
#                     if node.left:
#                         node = node.left
#                         pass
#                     else:
#                         node.left = TreeNode(val)
#                         break
#             return root
#         else:
#             return TreeNode(val)
def insert(root,val):
    if not root:
        return TreeNode(val)
    if root.val>val:
        root.left=insert(root.left,val)
    else:
        root.right=insert(root.right,val)
    return root
class Solution:
    
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        return insert(root,val)
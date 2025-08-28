#logic:left-node-right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        result = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)    
            result.append(node.val) 
            inorder(node.right)    
        inorder(root)
        return result
        
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)      #tree type input 
sol=Solution()
print(sol.inorderTraversal(root))

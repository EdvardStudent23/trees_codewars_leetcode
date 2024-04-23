'''
Module for deleting a certain node
'''
class Solution:
    '''
    Solution class
    '''
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        '''
        Function deletes a node
        '''
        if not isinstance(root, TreeNode):
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key) 
        elif key < root.val:
            root.left = self.deleteNode(root.left, key) 
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            
            suc = root.right
            par = root
            while suc.left:
                suc = suc.left
                par = suc
            root.val = suc.val

            if par.right == suc:
                par.right = self.deleteNode(par.right, suc.val)
            elif par.left == suc:
                par.left = self.deleteNode(par.left, suc.val)
        return root
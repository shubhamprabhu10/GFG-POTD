class Solution:    
    def findPreSuc(self, root, pre, suc, key):            
        def inorder(root,pre,suc,k):
            if root == None:
                return
            if root.key ==k:
               inorder(root.left,pre,suc,k)
               inorder(root.right,pre,suc,k)
            if root.key<k:
                pre[0]=root
                inorder(root.right,pre,suc,k)
            if root.key>k:
                suc[0]=root
                inorder(root.left,pre,suc,k)
        predecessor=[pre]
        successor=[suc]
        inorder(root,predecessor,successor,key)        
        return predecessor[0],successor[0]

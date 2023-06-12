
class Solution:
    def check(self,node,mini,maxi):       
        if node is None:
            return True
        
        if node.data < mini or node.data > maxi:
           return False
        return (self.check(node.left, mini, node.data - 1) and
            self.check(node.right, node.data+1, maxi))
     
    def solve(self,root,ans,target,k):
        maxi=4294967296
        mini = -4294967296
        if root==None:
            return (0,0)
        left,l=self.solve(root.left,ans,target,k)
        right,r=self.solve(root.right,ans,target,k)
        
        if left+right+root.data==target and self.check(root,mini,maxi)==True :
            if self.s  > l+r+1:
                self.s=l+1+r                                     
        return (left+right+root.data, l+r+1 )
    
    def minSubtreeSumBST(self, target, root):
        
        self.s=10000   
        ans,s=self.solve(root,0,target,0)        
        if self.s==10000:
            return -1
        return self.s

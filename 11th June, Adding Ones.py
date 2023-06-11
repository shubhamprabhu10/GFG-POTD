class Solution:
    def update(self, a, n, updates, k):    
        for i in updates:
            a[i-1]+=1
        temp=0
        for j in range(n):
            a[j]+=temp
            temp=a[j]
        return (a)

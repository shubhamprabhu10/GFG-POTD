class Solution:
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        ind=[0]*(V)
        for i in adj:
            for j in i:
                ind[j]+=1
        queue=[]
        res=[]
        for i in range(len(ind)):
            if ind[i]==0:
                queue.append(i)
        while queue:
            curr=queue.pop()
            res.append(curr)
            for j in adj[curr]:
                ind[j]-=1
                if ind[j]==0:
                    queue.append(j)
        return res

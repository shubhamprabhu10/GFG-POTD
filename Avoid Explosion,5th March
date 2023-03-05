class Solution:
    def avoidExlosion(self, mix, n, danger, m):
        #code here
        check=set([])
        ans=[]
        for i in mix:
            c=0
            i1=[i[1],i[0]]
            if i in danger or i1 in danger:
                ans.append("No")
                c=1
            else:
                if i[0] in check:
                    for j in check:
                        l=[j,i[1]]
                        l1=[i[1],j]
                        if l in danger or l1 in danger:
                            ans.append("No")
                            c=1
                            break
                if c==0:
                    check.add(i[0])
                    check.add(i[1])
                    ans.append("Yes")
        return ans

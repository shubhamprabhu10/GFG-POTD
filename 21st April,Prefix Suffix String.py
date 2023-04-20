class Solution:
    def prefixSuffixString(self, s1, s2) -> int:
        #code here
        c=0
        j=0
        for i in s2:
            while(j<len(s1)):
                if(s1[j].startswith(i) or s1[j].endswith(i)):
                    c=c+1
                    break
                j=j+1
        return(c)

class Solution:
    def maxEqualSum(self, N1:int,N2:int,N3:int, S1 : List[int], S2 : List[int], S3 : List[int]) -> int:
        # code here
        s1 = sum(S1)
        s2 = sum(S2)
        s3 = sum(S3)
        top = 0
        top1 = 0
        top2 = 0
        while True:
            if top == N1 or top1 == N2 or top2 == N3:
                return 0
            if s1 == s2 and s2 == s3:
                return s1
            if s1 >= s2 and s1 >= s3:
                s1 = s1 - S1[top]
                top += 1
            elif s2 >= s1 and s2 >= s3:
                s2 = s2 - S2[top1]
                top1 += 1
            elif s3>=s1 and s3>=s2:
                s3 = s3 - S3[top2]
                top2 += 1
        return 0

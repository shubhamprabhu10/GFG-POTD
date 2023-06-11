from itertools import permutations
class Solution:
    def find_permutation(self, S):
        # Code here
        temp = []
        for i in permutations(sorted(S)):
            if ''.join(i) not in temp:
                temp.append(''.join(i))
        return temp       

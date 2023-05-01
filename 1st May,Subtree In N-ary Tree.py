class Solution:
    def __init__(self):
        self.ans = 0
        self.m = {}

    def solve(self, root):
        if not root:
            return ""

        s = str(root.key) + " "
        for c in root.children:
            s += self.solve(c) + " "

        if s in self.m and self.m[s] == 1:
            self.ans += 1
        self.m[s] = self.m.get(s, 0) + 1

        return s

    def duplicateSubtreeNaryTree(self, root):
        self.solve(root)
        return self.ans

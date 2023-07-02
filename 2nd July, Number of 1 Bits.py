class Solution:
    def setSetBit(self, x, y, l, r):
          bitMask = ((1 << (r - l + 1)) - 1) << (l - 1)
          bits = y & bitMask
          x = x | bits
          return x

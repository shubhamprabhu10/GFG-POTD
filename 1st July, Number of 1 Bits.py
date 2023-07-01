class Solution:
	def setBits(self,n):
		x=str(bin(n).replace("0b", ""))
		return x.count("1")

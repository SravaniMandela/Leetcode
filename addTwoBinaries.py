class Solution(object):
    def addBinary(self, a, b):
        a=bin(int(a,2)) #str to int type
        b=bin(int(b,2))
        a=int(a,2)    # converted binary to int
        b=int(b,2)
        c=a+b
        return bin(c)[2:]
        

a='11'
b='1'
sol=Solution()
print(sol.addBinary(a, b))

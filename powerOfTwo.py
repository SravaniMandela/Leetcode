class Solution(object):
    def isPowerOfTwo(self, n):
        for i in range(0,(n//2)+1):
            if((2**i)==n):
                return True
            if(2**i > n):
                return False
        return False
                       
n=262143
sol=Solution()
print(sol.isPowerOfTwo(n))
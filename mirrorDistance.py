#rev of 25 is 52 so abs(25-52) is 27 
class Solution(object):
    def mirrorDistance(self, n):
        rev=""
        for i in str(n):
            rev=i+rev
        a=int(rev)
        return abs(n-a)
        
n=25        
sol=Solution()
print(sol.mirrorDistance(n))
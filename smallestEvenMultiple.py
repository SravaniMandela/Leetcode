#If n%2 is 0 then return n else nx2 to get the smallest even multiple(lcm of 2 and n)
class Solution(object):
    def smallestEvenMultiple(self, n):
        if(n%2==0):
            return n
        else:
            return n*2
            
n=6  
sol=Solution()
print(sol.smallestEvenMultiple(n))
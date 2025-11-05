#see the problem desscription in leetcode
class Solution(object):
    def arrangeCoins(self, n):
        if(n==1 or n==2):
            return 1
        rows=0
        for i in range(1,n+1):
            if(n-i==0):
                return rows+1
            if(n-i<0):
                return rows
            n=n-i
            rows=rows+1
n=10
sol=Solution()
print(sol.arrangeCoins(n))
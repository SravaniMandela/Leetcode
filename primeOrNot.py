class Solution(object):
    def primeNumber(self, num):
        c=0
        for i in range(1,num+1):
            if(num%i==0):
                c=c+1
        if(c==2):
            return True
        else:
            return False
num = 1
sol = Solution()
print(sol.primeNumber(num))
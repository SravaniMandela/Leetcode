class Solution(object):
    def checkPerfectNumber(self, num):
        if(num<=0):
            return False
        total=0
        for i in range(1,(num//2)+1):
            if(num%i==0):
                total+=i
        if(total==num):
            return True
        return False
            
        
num = 7        
sol=Solution()
print(sol.checkPerfectNumber(num))

#ex:28 = all positive divisors of 28 are 1,2,4,7,14 and itself(but remove itself) now 1+2+4+7+14=28 so true
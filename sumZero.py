#you have to take n values and it should sum upto 0 so i took pairs ex:+3,-3 likewise if n is odd i'm appending 0
class Solution(object):
    def sumZero(self, n):
        a=[]
        if(n%2==1):
            a.append(0)
        i=1
        while(len(a)<n):
            a.append(i)
            a.append(-i)
            i+=1
        return a
            
       
n=5 #output: [0,+1,-1,+2,-2]
sol=Solution()
print(sol.sumZero(n))
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

#n=4 output=3+2=>5, n=5 output=5+3=>8

#likewise if you calculate for each step u'll get fibonacci series 1,2,3,5,8...

class Solution(object):
    def climbStairs(self, n):
        if(n==0):
            return 0
        if(n==1):
            return 1
        if(n==2):
            return 2
        else:
            fib_series=[0,1,2]
            s=0
            for i in range(3,n+1):
                s=fib_series[i-1]+fib_series[i-2]
                fib_series.append(s)
            return fib_series[-1]
        
n=5        
sol=Solution()
print(sol.climbStairs(n))
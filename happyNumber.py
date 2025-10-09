class Solution(object):
    def isHappy(self, n):
        set_a=set()
        if(n<=0):
            return False
        while n not in set_a and n != 1:
            s=0
            set_a.add(n)
            n=str(n)
            for i in n:
                s=s+(int(i)*int(i))
            n=s
        if n == 1:
            return True
        else:
            return False
                       
n=4
sol=Solution()
print(sol.isHappy(n))


#added set() to keep track of repetitive values just to stop infinite loop (example of n=4)

#see the program description in leetcode for happy number 


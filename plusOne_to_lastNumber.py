class Solution(object):
    def plusOne(self, digits):
        carry=1
        for i in range(len(digits)-1,-1,-1):
             digits[i]+=carry
             if digits[i]==10:
                 digits[i]=0
                 carry=1
             else:
                 carry=0
                 break
        if carry==1:
            digits.insert(0,1)           #insert 1 at 0th place Or digits=[1]+digits this also works
        return digits

digits = [1,9]     #output = [2,0]
digits = [9,9]      #output=[1,0,0]
digits = [1,2,3]    #output=[1,2,4]
digits = [9]       #output = [1,0]
sol=Solution()
print(sol.plusOne(digits))

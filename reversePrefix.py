class Solution(object):
    def reversePrefix(self, s, k):
        rev=""
        for i in range(k):
            rev=s[i]+rev
        return rev+s[len(rev):]
            
s = "abcd"
k = 2    
#output: bacd reverse only k no. of letters      
sol=Solution()
print(sol.reversePrefix(s,k))
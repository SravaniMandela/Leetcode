class Solution(object):
    def reverseString(self, s):
        rev=[]
        for i in s:
            rev=[i]+rev
        for i in range(len(s)):
            s[i] = rev[i]
        return s
            
        
s = ["h","e","l","l","o"]        
sol=Solution()
print(sol.reverseString(s))
class Solution(object):
    def reverseString(self, s):
        rev=[]
        for i in s:
            rev=[i]+rev
        s[:]=rev
        return s
        
s = ["h","e","l","l","o"]
sol=Solution()
print(sol.reverseString(s))
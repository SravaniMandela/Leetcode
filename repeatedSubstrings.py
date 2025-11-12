class Solution(object):
    def repeatedSubstringPattern(self, s):
            for j in range(1,(len(s)//2)+1):
                if(len(s)%j==0):
                    b=s[:j]*(len(s)//j)
                    if(s==b):
                        return True
            return False
        
s = "abab"
sol = Solution()
print(sol.repeatedSubstringPattern(s))


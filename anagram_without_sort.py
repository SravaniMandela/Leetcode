class Solution(object):
    def isAnagram(self, s, t):
        if(len(t)!=len(s)):
            return False
        t=list(t)
        for i in s:
            if i in t:
                t.remove(i)
            else:
                return False
        if(len(t)==0):
            return True

s = "anagram"
t = "nagaram"
sol=Solution()
print(sol.isAnagram(s,t))
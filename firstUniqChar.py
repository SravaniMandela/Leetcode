class Solution(object):
    def firstUniqChar(self, s):

        for i in range(len(s)):
            c=0
            for j in range(len(s)):
                if i!=j and s[i]==s[j]:
                    c=c+1
            if(c==0):
                return i
        return -1
                    
s = "aabb"
sol=Solution()
print(sol.firstUniqChar(s))

#s="loveleetcode" output:2 coz v count is 0 in this string
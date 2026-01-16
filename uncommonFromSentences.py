class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        s1=s1.split()
        s2=s2.split()
        for i in s1[:]:
            if i in s2:
                s2.remove(i)
                s1.remove(i)
        return s1+s2
        
s1 = "apple apple"
s2 = "banana"     
sol=Solution()
print(sol.uncommonFromSentences(s1,s2))
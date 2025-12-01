class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        magazine=list(magazine)
        for ch in ransomNote:
            if ch not in magazine:
                return False
            magazine.remove(ch)
        return True
            
            
        
ransomNote = "aa"
magazine = "ab"
sol=Solution()
print(sol.canConstruct(ransomNote, magazine))

#check whether can we able to construct ransomnote with the letter in magazine
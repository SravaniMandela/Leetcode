class Solution(object):
    def isLongPressedName(self, name, typed):
        j=0
        for i in range(len(typed)):
            if(j<len(name) and typed[i]==name[j]):
                j=j+1
            elif(i>0 and typed[i]==typed[i-1]):
                continue
            else:
                return False
        return j==len(name)
                
name = "saeed"
typed = "ssaaedd"   
sol=Solution()
print(sol.isLongPressedName(name, typed))
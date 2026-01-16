class Solution(object):
    def isLongPressedName(self, name, typed):
        name=list(name)
        typed=list(typed)
        for i in name:
            if i in typed:
                typed.remove(i)
        print(typed)
        return False
                
name = "saeed"
typed = "ssaaedd"   
sol=Solution()
print(sol.isLongPressedName(name, typed))
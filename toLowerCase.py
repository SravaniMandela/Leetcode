# capital letter will be in between 65 to 90 and to convert that capital letter to small we have to add +32. 
# ord(letter) gives its value and chr(ord(letter)) converts that number to character
class Solution(object):
    def toLowerCase(self, s):
        res=""
        for i in s:
            if(ord(i)>=65 and ord(i)<=90):
                res=res+chr(ord(i)+32)
            else:
                res=res+i
        return res
s = "Hello"
sol=Solution()
print(sol.toLowerCase(s))
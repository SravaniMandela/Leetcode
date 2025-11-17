#First store all the characters into a list (rev_s) and just reverse it and for each letter in s, if it 
# is a character just add each letter which was stored in the list to the empty string(res)

class Solution(object):
    def reverseOnlyLetters(self, s):
        rev_s=[]
        for i in s:
            if i.isalpha():
                rev_s.append(i)
        rev_s=rev_s[::-1]
        idx=0
        res=""
        for i in s:
            if i.isalpha():
                res=res+rev_s[idx]
                idx+=1
            else:
                res=res+i
        return res
s = "a-bC-dEf-ghIj"
sol = Solution()
print(sol.reverseOnlyLetters(s))
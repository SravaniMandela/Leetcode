#reverse all words in a sentence
class Solution(object):
    def reverseWords(self, s):
        rev=""
        for i in s:
            rev=i+rev
        print(rev)  #rev=gniD rM
        new_rev=[]
        rev=rev.split()
        print(rev) #rev=['gniD', 'rM']
        for i in rev:
            new_rev=[i]+new_rev
        s=" ".join(new_rev)  #converting back to string 
        return s
        
s = "Mr Ding"
sol=Solution()
print(sol.reverseWords(s))

#reverse one word
# class Solution(object):
#     def reverseWords(self, s):
#         rev=""
#         #s=s.split()
#         print(s)
#         for i in s:
#             rev=i+rev
#         s=rev
#         return s
        
# s = "Mr"
# sol=Solution()
# print(sol.reverseWords(s))
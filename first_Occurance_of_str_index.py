#find will retrun the index if string is found
class Solution(object):
    def strStr(self, haystack, needle):
           return haystack.find(needle)
           
haystack="butsad"
needle="sad"
sol = Solution()
print(sol.strStr(haystack, needle))

#length of last word in a string, strip actually removes all the leading and trailing spaces
class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.strip().split(" ")
        return len(s[-1])

sol = Solution()
s = "   fly me   to   the moon  "
print(sol.lengthOfLastWord(s))
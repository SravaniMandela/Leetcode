#need to consider only alpha numeric
import re

class Solution(object):
    def isPalindrome(self, s):
        rev = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return rev == rev[::-1]
s = "0P"
sol = Solution()
print(sol.isPalindrome(s))
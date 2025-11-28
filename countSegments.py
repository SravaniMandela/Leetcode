class Solution(object):
    def countSegments(self, s):
        s = s.strip()
        if len(s) == 0:
            return 0
        return len(s.split())


s="Of all the gin joints in all the towns in all the world,   "
sol=Solution()
print(sol.countSegments(s))

#empty spaces at last shouldn't be counted
#just this line works:  return len(s.split()) , split s based on white space and removes any trailing whitespaces at the end
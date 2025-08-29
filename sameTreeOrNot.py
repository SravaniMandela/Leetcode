class Solution(object):
    def isSameTree(self, p, q):
        if(str(p)==str(q)):
            print(str(p))
            return True
        else:
            return False
p = [1,2,3]
q = [1,2,3]
sol=Solution()
sol.isSameTree(p,q)

# Input: p = [1,2], q = [1,null,2]
# Output: false
        

        
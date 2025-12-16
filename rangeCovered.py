class Solution(object):
    def isCovered(self, ranges, left, right):
        for i in range(left,right+1):
            covered = False
            for start,end in ranges:
                if start <= i <= end:
                    covered = True
                    break
            if not covered:
                return False
        return True
     
ranges = [[1,2],[3,4],[5,6]]
left = 2
right = 5
sol=Solution()
print(sol.isCovered(ranges, left, right))
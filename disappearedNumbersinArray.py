class Solution(object):
    def findDisappearedNumbers(self, nums):
        a=[]
        b=set(nums)
        for i in range(1,len(nums)+1):
            if i not in b:
                a.append(i)
        return a
                
nums = [4,3,2,7,8,2,3,1]
sol = Solution()
print(sol.findDisappearedNumbers(nums))

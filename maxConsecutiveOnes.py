class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        c=0
        a=[]
        for i in range(len(nums)):
            if(nums[i]==1):
                c+=1
            else:
                a.append(c)
                c=0
        a.append(c)
        return max(a)
nums = [1,0,1,1,0,1]
sol=Solution()
print(sol.findMaxConsecutiveOnes(nums))
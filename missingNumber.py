class Solution(object):
    def missingNumber(self, nums):
        larg=nums[0]
        for i in range(len(nums)):
            if(nums[i]>larg):
                larg=nums[i]
        for i in range(0,larg):
            if i not in nums:
                return i
        return larg+1
            
                       
nums=[9,6,4,2,3,5,7,0,1]
sol=Solution()
print(sol.missingNumber(nums))
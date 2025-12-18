class Solution(object):
    def createTargetArray(self, nums, index):
        target=[]
        for i in range(len(nums)):
            target.insert(index[i],nums[i])
        return target
        
        
nums = [1,2,3,4,0]
index = [0,1,2,3,0]       
sol=Solution()
print(sol.createTargetArray(nums,index))
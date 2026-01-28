#Find the largest and smallest numbers just increment the k value to smallest and decrement the k value to largest 
# so that difference will be closer(smallest) and just return the difference if greater than 0 else 0
class Solution(object):
    def smallestRangeI(self, nums, k):
        maxi=nums[0]
        mini=nums[0]
        for i in nums:
            if(i>maxi):
                maxi=i
            if(i<mini):
                mini=i
        maxi=maxi-k
        mini=mini+k
        result=maxi-mini
        if(result>0):
            return result
        else:
            return 0
        

nums = [0,10]
k = 2        
sol=Solution()
print(sol.smallestRangeI(nums, k))
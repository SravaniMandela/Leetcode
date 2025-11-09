class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        for i in range(len(nums)):
           for j in range(i+1,len(nums)):
               if(nums[i]==nums[j]):
                   if(j-i<=k):
                       return True
        return False
           
nums = [1,2,3,1,2,3]
k=2
sol = Solution()
print(sol.containsNearbyDuplicate(nums, k))

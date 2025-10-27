#Given an integer array nums, return true if any value appears at least twice in the array, and return false if 
# every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        if(len(nums)!=len(set(nums))):
            return True
        else:
            return False
nums=[1,2,3,1]
sol=Solution()
print(sol.containsDuplicate(nums))
#remove deplicates INPLACE means we should not use new array. As it is a sorted list so first element is always unique thatswhy i 
#start from second element(i=1 and k=1 as count) and check if it is equal to previous element if yes then remove it
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        k=1
        for i in range(1,len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k=k+1
        return k

sol = Solution()
nums=[1,1]
k=sol.removeDuplicates(nums)
print(k)
print(nums[:k])

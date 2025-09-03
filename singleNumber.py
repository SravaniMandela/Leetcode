#every number comes twice so just return the single number
class Solution(object):
    def singleNumber(self, nums):
        for i in range(len(nums)):
            c=0
            for j in range(len(nums)):
                if(nums[i]==nums[j]):
                    c=c+1
            if(c==1):
                return nums[i]
nums = [2,2,1]
sol = Solution()
print(sol.singleNumber(nums))

#same number tho xor chesthe 0 vasthadhi
# same program with less time and space complexity using xor
class Solution(object):
    def singleNumber(self, nums):
        res=0
        for i in nums:
            res=res^i
        return res
            
nums = [4,1,2,1,2]
sol = Solution()
print(sol.singleNumber(nums))

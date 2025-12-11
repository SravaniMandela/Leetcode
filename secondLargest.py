class Solution(object):
    def secondLarge(self, nums):
        largest=nums[0]
        sec_larg=0
        for i in nums:
            if(i>largest):
                sec_larg=largest
                largest=i
            elif i<largest and i>sec_larg:
                sec_larg = i
        return sec_larg
nums = [3,2,1]
sol=Solution()
print(sol.secondLarge(nums))
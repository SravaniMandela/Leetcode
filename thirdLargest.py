class Solution(object):
    def thirdMax(self, nums):
        nums=set(nums)
        largest=nums[0]
        sec_larg=0
        third_larg=0
        for i in nums:
            if(i>largest):
                third_larg=sec_larg
                sec_larg=largest 
                largest=i 
            elif i<largest and i>sec_larg: 
                third_larg=sec_larg
                sec_larg=i
            elif i<sec_larg and i>third_larg: 
                third_larg=i 
        if(third_larg==0):
            return largest
        return third_larg
nums = [1,2,2,3,5,3,5]
sol=Solution()
print(sol.thirdMax(nums))
class Solution(object):
    def moveZeroes(self, nums):
        num=[]
        c=0
        for i in range(len(nums)):
            if(nums[i]==0):
                c=c+1
            if(nums[i]!=0):
                num.append(nums[i])
        for i in range(0,c):
            num.append(0)
        for i in range(len(nums)):
            nums[i] = num[i]
        return nums

nums = [0,1,0,3,12]
sol = Solution()
print(sol.moveZeroes(nums))

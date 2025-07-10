class Solution(object):
    def twoSum(self, nums, target):
        new_nums=[]
        for i in range(len(nums)):
            print(i)
            for j in range(i+1,len(nums)):
                    print(j)
                    if nums[i]+nums[j] == target:
                        new_nums.append(nums[i])
                        new_nums.append(nums[j])
                        return new_nums
nums=[11,15,2,7]
#nums=[1,8,2,7,3,6]
target = 9 
solution = Solution()
print(solution.twoSum(nums, target))
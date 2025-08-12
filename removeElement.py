#number which equal val has to be removed from nums
#taking new_nums
class Solution(object):
    def removeElement(self, nums, val):
        new_nums=[]
        for i in range(len(nums)):
            if(nums[i]!=val):
                new_nums.append(nums[i])
        print(len(new_nums), end=" ")
        print(new_nums)
        return new_nums
nums = [0,1,2,2,3,0,4,2]
val = 2       
sol=Solution()
sol.removeElement(nums, val)


#without changing nums
class Solution(object):
    def removeElement(self, nums, val):
        k=0
        for i in range(len(nums)):
            if(nums[i]!=val):
                nums[k]=nums[i]
                k+=1
        print(k,nums)
        return k
nums = [0,1,2,2,3,0,4,2]
val = 2       
sol=Solution()
k=sol.removeElement(nums, val)
print("k:", k)
print("Nums after:", nums[:k])
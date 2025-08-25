#add elements only till m,n in nums1,nums2 
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1_new = []
        for i in range(m): 
            nums1_new.append(nums1[i])
        for j in range(n): 
            nums1_new.append(nums2[j])
        nums1_new.sort()
        nums1[:] = nums1_new 
        return nums1
                    
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3       
sol=Solution()
print(sol.merge(nums1, m, nums2, n))
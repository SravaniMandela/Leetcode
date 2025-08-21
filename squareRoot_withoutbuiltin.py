class Solution(object):
    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x
        low = 0
        high = x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
            else:
                high = mid - 1
        return high 

x = 8
sol = Solution()
print(sol.mySqrt(x))

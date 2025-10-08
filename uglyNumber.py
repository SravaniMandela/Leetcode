#divide until and unless number gets divisible by 2,3 and 5
class Solution(object):
    def isUgly(self, n):
        if(n<=0):
            return False
        while n%2==0:
            n=n//2
        while  n%3==0:
            n=n//3
        while n%5==0:
            n=n//5
        if n == 1:
            return True
        else:
            return False
                       
n=1
sol=Solution()
print(sol.isUgly(n))


# ex:n=8 : 8/2=4/2=2/2=1 so 8 is ugly num
# ex:n=14: 14/2 =7 : 7 not equals 1 so 7 14 is not ugly
# ex:n=6: 6/2 =3: 3/3 =1 so 6 is ugly
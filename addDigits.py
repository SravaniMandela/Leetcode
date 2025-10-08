class Solution(object):
    def addDigits(self, num):
        a=["num"]
        if(num<10):
            return num
        else:
            while(num>10):
                digits_sum=0
                for i in a:
                    print(i)
                       
            
num=38
sol=Solution()
print(sol.addDigits(num))
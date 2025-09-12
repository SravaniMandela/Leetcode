1)str = "http://string/com"
str = str.replace("/", ":")
print(str)

2)str="P@$$word"
special_chars=""
for char in str:
    if not char.isalnum():
        special_chars+=char
print(special_chars)

3)c=[1,2,3,4,5]
b=[2,3,4,1,6]
a=[]
for i in c:
    if i in b:
        a.append(i)
print(a)

4)c = [15432, 12345, 54321]
sum=0
for number in c:
    b=str(number)[-2]
    sum = sum+int(b)
print(sum)

4)c = ["5432","2345","2341"]
sum=0
for number in c:
    b=number[-2]
    sum = sum+int(b)
print(sum)

5)c = ["abcda", "aerfaq", "aasfasa"]
for string in c:
    count_a = string.count('a')  # Count the occurrences of 'a' in the string
    print(f"The letter 'a' occurs {count_a} times in '{string}'")

5)c = ["abcda", "aerfaq", "aasfasa"]
for i in c:
    c=0
    for j in i:
        if(j=="a"):
            c=c+1
    print(c)

7)str="https://google/com/sravani"
str=str.split("/")
print(str[-1])

8)fibonacci:nth number
a=1
b=1
n=7
for i in range(n-2):
    c=a+b
    a=b
    b=c
print(c)

8)def fibonacci(n):
    if(n==0):
        return 1
    if(n==1):
        return 1
    else:
        fib_series=[1,1]
        for i in range(2,n):
            fib=fib_series[i-1]+fib_series[i-2]
            fib_series.append(fib)
        return fib_series
start=10
n=15
s=fibonacci(n)
print(s[start:])

8)def fibonacci_series(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    else:
        return fibonacci_series(n-1)+fibonacci_series(n-2)
n=9
for i in range(n):
    print(fibonacci_series(i))
print(fibonacci_series(n))

9)a="madam"
b=a[::-1]
if(a==b):
    print(a,"is palindrome")

10)a="madam"
b=""
for i in a[::-1]:
    if i:
        b=b+i
if(a==b):
    print(a,"is palindrome")


11)a=12321
b=str(a)
rev_a=""
for i in b:
    rev_a=i+rev_a
if(a==int(rev_a)):
    print(a,"is palindrome")

11)def reverse_number_math(n):
    """Reverses an integer using mathematical operations."""
    reversed_num = 0
    while n > 0:
        digit = n % 10 
        reversed_num = reversed_num * 10 + digit 
        n = n // 10 
    return reversed_num
number = 12345
print(f"The reverse of {number} is {reverse_number_math(number)}")


12)factorial
def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
n=3
result=fact(n)
print(result)

   
13)largest num in list:
nums=[2,45,62,1]
largest=nums[0]
for i in nums:
    if i>largest:
        largest=i
print(largest)

14)#count the freq of each ele in a list
nums=[1,2,1,2,3,4,5,5,5,6]
dict={}
for i in nums:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
print(dict)

15)nums=[2,45,62,1]
largest=nums[0]
sec_largest=largest
for i in nums:
    if i>largest:
        sec_largest=largest
        largest=i
print(sec_largest)

16)#remove duplicates from a list
nums=[1,2,3,1,2,3,8]
c=[]
for i in nums:
    if i not in c:
        c.append(i)
print(c)

17)import json

# Define the dictionaries
a = {"details": "100,sravani,nap"}
b = {"details2": "200,sravan,napier"}

# Convert the dictionaries to JSON format and print them
print(json.dumps(a, indent=4))
print(json.dumps(b, indent=4))

18)print number range
class Solution(object):
    def primeNumber(self, num):
        for i in range(2,num+1):
            c=0
            for j in range(1,i+1):
                if(i%j==0):
                    c=c+1
            if(c==2):
                print(i)
num = 20
sol = Solution()
sol.primeNumber(num)

19)is prime or Not:
class Solution(object):
    def primeNumber(self, num):
        c=0
        for i in range(1,num+1):
            if(num%i==0):
                c=c+1
        if(c==2):
            return True
        else:
            return False
num = 1
sol = Solution()
print(sol.primeNumber(num))

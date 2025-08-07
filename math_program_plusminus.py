# calculate the ratios of its elements that are positive,negative and zero. Print the decimal value of each fraction on a new line 
# with 6 places after the decimal.
import math
def plusMinus(arr):
    p=z=m=0
    for i in range(n):
        if arr[i]>0:
            p=p+1
        elif arr[i] < 0:
            m=m+1
        else:
            z=z+1
    print(f"{p/n:.6f}")
    print(f"{z/n:.6f}")
    print(f"{m/n:.6f}")
n = 5
arr = [-1,1,0,2,-2]
plusMinus(arr)

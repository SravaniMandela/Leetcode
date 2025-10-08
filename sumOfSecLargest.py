s=["123","436","654","652"]
a=[]
for i in s:
    maxi=-1
    sec_lar=-1
    for j in i:
        j=int(j)
        if(j>maxi):
            sec_lar=maxi 
            maxi=j 
        elif(j>sec_lar and j<maxi): #for 652 case
            sec_lar=j
    a.append(sec_lar)
print(a)
s=0
for i in range(len(a)):
    s=s+a[i]
print(s)
    

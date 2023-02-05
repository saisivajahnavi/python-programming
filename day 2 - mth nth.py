n=int(input("enter the number: "))
l=[]
for i in range(n):
    l.append(int(input("enter the elements: ")))
a=int(input("m: "))
b=int(input("n: "))
l=sorted(l)
print("mth maximum=",l[-a])
print("nth minimum=",l[b-1])
print("sum=",l[b-1]+l[-a],"diff=",l[-a]-(l[b-1]))

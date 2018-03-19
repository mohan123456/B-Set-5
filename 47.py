#47
a=[]
n=int(input("enter n:"))
for i in range(0,n):
  b=int(input())
  a.append(b)
a.sort()
print(a[0],a[n-1])

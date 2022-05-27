N=int(input());b=input();a=[]
for i in b:
    if not i==" ":
        a.append(int(i))
for j in range(1,N):
    i=j-1
    key=a[j]
    while i>=0 and a[i]>key:
        a[i+1]=a[i]
        i-=1
    a[i+1]=key
for i in a:
    print(i,end=" ")

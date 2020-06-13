l=int(input(""))
ar=list(map(int,input("").split()))
z=[ar[0]]
count=0
for i in range(1,len(ar)):
    if(ar[i]>max(z) or ar[i]<min(z)):
        count=count+1
    z.append(ar[i])

print(count)

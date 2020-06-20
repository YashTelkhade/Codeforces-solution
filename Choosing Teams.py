x,y=map(int,input().split())
ar=list(map(int,input().split()))
ar.sort()
for i in range(len(ar)):
    ar[i]=ar[i]+y
count=0
for i in ar:
    if(i<=5):
        count=count+1

print(int(count/3))

x,y=map(int,input().split())
l=list(map(int,input().split()))
count=0
prev=1

for i in l:
    count+=(i-prev)%x
    prev=i
print(count)

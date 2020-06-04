n=int(input(""))
ar = list(map(int, input().strip().split(' '))) 
max=0
cnt=1
 
for i in range (0,n-1):
    if(ar[i]>ar[i+1]):
        if(cnt>max):
            max=cnt
        cnt=1
    else:
        cnt=cnt+1
 
if(cnt>max):
    max=cnt
 
print(max)

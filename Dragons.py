x,y=map(int,input().split())
l=[]
j=0
for i in range(y):
    a,b=map(int,input().split())
    l.append((a,b))
    
l.sort()
count=0
for i in range(len(l)):
    if(x>l[i][0]):
        x=x+l[i][1]
    else:
       count=1
       break
   
if(count==0):
    print("YES")
else:
    print("NO")

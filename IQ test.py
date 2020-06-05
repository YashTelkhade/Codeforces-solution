x=int(input(""))
ar=list(map(int, input().strip().split(' ')))
o=0
p=0

z=[]
for i in range(0,len(ar)):
    for j in range(0,len(ar)):
        z.append((ar[i]-ar[j]))
        
    z.remove(0)
    
    
    for k in z:
        if(k%2==0):
            o=1
        else:
            p=1
        
    
    if(o==1 and p==1):
        z.clear()
        o=0
        p=0
    else:
        print(i+1)
    

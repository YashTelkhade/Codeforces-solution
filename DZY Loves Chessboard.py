n,m=[int(x) for x in input("").split()]
l=[]
for i in range(0,n):
    ar=list(str(input("")))
    if(i%2==0):
        for j in range(m):
            if(j%2==0 and ar[j]=="."):
                ar[j]="B"
            elif(j%2!=0 and ar[j]=="."):
                ar[j]="W"
    else:
        for j in range(m):
            if(j%2==0 and ar[j]=="."):
                ar[j]="W"
            elif(j%2!=0 and ar[j]=="."):
                ar[j]="B"
        
    l.append(ar)    
    
for i in l:
    s=""
    for x in i:
        s=s+x
    print(s)
   

        

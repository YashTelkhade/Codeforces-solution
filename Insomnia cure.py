def jury(c):
    for j in range(1,l[-1]+1):
        if(j%c==0):
            x.append(j)

l=[]
for i in range (0,5):
    j=int(input(""))
    l.append(j)
    
x=[]

for i in range(0,len(l)-1):
    jury(l[i])
    
    
k=set(x)
print(len(k))        

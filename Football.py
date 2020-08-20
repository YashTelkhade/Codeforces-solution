n=int(input(""))
l=[]
for i in range(0,n):
    ar=str(input(""))
    l.append(ar)    
    
p={}
for i in l:
    if i in p:
        p[i]+=1
    else:
        p[i]=1
        
sort = sorted(p.items(), key=lambda x: x[1])
print(sort[-1][0])

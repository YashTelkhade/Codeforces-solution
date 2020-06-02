n=int(input(""))
ar=list(map(int, input().strip().split(' '))) 

l=[]
j=1

for i in range(0,len(ar)):
    l.append(j)
    l.append(ar[i])
    j=j+1
    
it = iter(l) 
dct = dict(zip(it,it))   
sort = sorted(dct.items(), key=lambda x: x[1])
z=[]

for i in range(0,len(sort)):
    z.append(sort[i][0])

k=""

for i in range(0,n):
    k=k+str(z[i])+" "

print(k)

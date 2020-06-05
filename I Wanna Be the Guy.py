x=int(input(""))
ar1=list(map(int, input().strip().split(' ')))
ar2=list(map(int, input().strip().split(' ')))

z=[]

for i in range(1,len(ar1)):
    z.append(ar1[i])
    
for i in range(1,len(ar2)):
    z.append(ar2[i])
    
k=set(z)

if(len(k)==x):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")

a,b = map(int,input().split())
ar=list(map(int,input("").split(' ')))
ar.sort()
l=[]
for i in range(a-1):
    l.append(ar[i+1]-ar[i])
if(len(l)>0):
    d=float(max(l)/2)
else:
    d=ar[0]

if(ar[0]-0<=d and b-ar[-1]<=d):
    print(float(d))
elif(ar[0]-0>d and ar[0]-0>b-ar[-1]):
    print(float(ar[0]-0))
else:
    print(float(b-ar[-1]))
    

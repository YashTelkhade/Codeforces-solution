x,y,z=[int(x) for x in input("").split()]
z=(z-(z%y)-x)
l=[]
if(z>0):
    l.append(z)
    while(z>y):
        z=z-y
        l.append(z)
    l.reverse()
    print(*l)
else:
    print(-1)

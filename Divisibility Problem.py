n=int(input(""))
l=[]
for i in range(n):
    a,b=[int(x) for x in input("").split()]
    z=((b-a%b)%b)
    l.append(z)

for i in l:
    print(i)

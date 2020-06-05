x= int(input(""))
ar=list(map(int, input().strip().split(' ')))
ar.sort()
z=""
for i in ar:
    z=z+str(i)+" "

print(z)

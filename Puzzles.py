x,y = [int(x) for x in input("").split()]
ar = list(map(int, input().strip().split(' ')))
ar.sort()
z=10000

for i in range(0,y-x+1):
    diff=ar[i+x-1] -ar[i]
    if diff<z:
        z=diff

print(z)

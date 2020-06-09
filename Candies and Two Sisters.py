import math
n=int(input(""))
for i in range(n):
    x=int(input(""))
    z=x-(x/2+1)
    if(z>0):
        print(math.ceil(z))
    else:
        print(0)

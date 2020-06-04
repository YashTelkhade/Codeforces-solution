n=int(input(""))
count=0
for i in range (0,n):
    x,y = [int(x) for x in input("").split()]
    if(y-x >=2):
        count = count +1
        
print(count)

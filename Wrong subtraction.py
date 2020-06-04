x,y = [int(x) for x in input("").split()]
 
while(y):
    y=y-1
    if(x%10==0):
        x=x/10
    else:
        x=x-1
        
print(int(x))

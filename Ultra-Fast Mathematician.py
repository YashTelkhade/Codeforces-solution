x= str(input(""))
y= str(input(""))
x=list(x)
y=list(y)

z=""
for i  in range(0,len(y)):
    if(int(x[i])+int(y[i]) == 1):
        z=z+"1"
    else:
        z=z+"0"
    
print(z)

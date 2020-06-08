x=list(str(input("")))
y=list(str(input("")))
z=list(str(input("")))

x=x+y
x.sort()
z.sort()

if(x==z):
    print("YES")
else:
    print("NO")

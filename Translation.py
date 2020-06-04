x=str(input(""))
y=str(input(""))
y=list(y)
y.reverse()
r="".join(y)

if(x==r):
    print("YES")
else:
    print("NO")

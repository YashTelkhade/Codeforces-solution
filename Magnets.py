n=int(input(""))
ar=[]
o=""
for i in range(0,n):
    j=str(input(""))
    o=o+j
    ar.append(j)

x="00"
y="11"

cx = o.count(x)
cy = o.count(y)

count=cx+cy
print(count+1)

n,m=[int(x) for x in input("").split()]
l=[]
for i in range(n):
    ar=list(map(int, input("").split()))
    l.append(ar)
dr=0
for i in l:
    if(i[0]==1 or i[m-1]==1):
         dr=1
zipped_rows = zip(*l)
t= [list(row) for row in zipped_rows]

for i in t:
    if(i[0]==1 or i[n-1]==1):
         dr=1
print([4,2][dr])

    

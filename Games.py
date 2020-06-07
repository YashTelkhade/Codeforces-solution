n=int(input(""))
l=[]
p=[]
for i in range(n):
    x,y=[int(x) for x in input("").split()]
    l.append(x)
    p.append(y)
    
count =0

for i in l:
    for j in p:
        if(i==j):
            count=count+1
            
print(count)

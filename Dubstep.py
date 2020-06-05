x= str(input(""))

l=x.split("WUB")
count=0
for i in l:
    if(i==''):
        count=count+1

for i in range (0,count):
    l.remove('')

z=""
for i in l:
    if(i !=" "):
        z=z+i+" "

print(z)

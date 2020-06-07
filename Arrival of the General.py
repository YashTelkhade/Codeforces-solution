n = int(input(""))
l = list(map(int,input().strip().split(' ')))

max=0
min=n-1

for i in range(n):
    if(l[i]>l[max]):
        max=i
    if(l[i]<=l[min]):
        min=i

if min>max:
	print (n-1-min+max)
else:
	print (n-1-min+max-1)

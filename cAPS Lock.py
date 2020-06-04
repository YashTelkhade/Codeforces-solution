s=str(input(""))

k=s.upper()

t=s.upper()
p=ord(t[0])
p=p+32
a=(chr(p))

for i in range(1,len(t)):
    a=a+t[i]


if(s==k):
    s=s.swapcase()
   
elif(s==a):
    s=s.swapcase()
  
print(s)
    

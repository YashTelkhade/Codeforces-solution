import math
n=int(input(""))
ar = list(map(int, input().strip().split(' '))) 

ar.sort()
ar.reverse()
s4=0
s3=0
s2=0
s1=0
taxi =0
for i in ar:
    if(i==4):
        s4=s4+1
    elif(i==3):
        s3=s3+1
    elif(i==2):
        s2=s2+1
    else:
        s1=s1+1
        

taxi = taxi+s4
if(s2%2 == 0):
    taxi=taxi + s2/2
else:
    taxi=taxi + s2/2+1
    if(s1>0):
        s1=s1-2

taxi = taxi +s3
if(s1>=s3>=0):
    s1=s1-s3
    if(s1>0):
        taxi = taxi + math.ceil(s1/4)
    
print(int(taxi))

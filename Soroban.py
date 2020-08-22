s=str(input(""))
s=list(s)
l=[]
for i in s:
    s=""
    if(int(i)>5):
        s=s+"-O|"
        j=int(i)-5
        s=s+"O"*j+"-"+"O"*(4-j)
    elif(int(i)<5):
        s=s+"O-|"
        j=int(i)
        s=s+"O"*j+"-"+"O"*(4-j)
    else:
        s=s+"-O|-OOOO"
    l.append(s)
    
l=l[::-1]  
for i in l:
    print(i)

    

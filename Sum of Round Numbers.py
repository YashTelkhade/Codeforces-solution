x=int(input(""))
cout=0
for i in range(x):
    l=[]
    if(cout==0):
        s=int(input(""))
        cout=1
    else:
        s=int(input("\n"))
    s=list(str(s))
    s.reverse()
    for i in range(0,len(s)):
         z=int(s[i])*(10**i)
         l.append(z)
    l=set(l)
    for j in l:
        if(j==0):
            l.remove(0)
            break
    print(len(l))
    for i in l:
        print(str(i)+" ",end='')
        

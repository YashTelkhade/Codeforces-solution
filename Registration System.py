x=int(input(""))
d={}
for i in range(x):
    s=str(input(""))
    if s in d:
        print(s + str(d[s]))
        (d[s])=(d[s])+1
    else:
        d[s]=1
        print("OK")

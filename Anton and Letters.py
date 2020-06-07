ar=set(input(""))
ar=set(ar)
ar.remove("{")
ar.remove("}")
my=" ,"

final=[each for each in ar if each in my]

if(len(final)>0):
    print(len(ar)-2)
else:
    print(len(ar))

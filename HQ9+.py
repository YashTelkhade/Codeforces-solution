x = str(input(""))
v="HQ9"

final= [each for each in x if each in v]
if(len(final) > 0):
    print("YES")
else:
    print("NO")

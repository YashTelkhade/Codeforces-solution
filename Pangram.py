n=int(input(""))
s=str(input(""))
s=s.lower()
ch="qwertyuiopasdfghjklzxcvbnm"

final = set([each for each in s if each in ch])

if(len(final)==26):
    print("YES")
else:
    print("NO")

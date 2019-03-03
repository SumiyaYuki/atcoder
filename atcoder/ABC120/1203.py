s=input()
a=0
b=0
for i in range(len(s)):
    if s[i]=='0':
        a=a+1
    else:
        b=b+1

if a>b:
    print(2*b)
else:
    print(2*a)

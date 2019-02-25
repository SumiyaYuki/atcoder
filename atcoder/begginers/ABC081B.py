n=input()
a=list(map(int,input().split()))

b=0
c=0

while b==0:
    for i in range(len(a)):
        a[i]=(a[i]/2)
        if a[i]!=int(a[i]):
            b=1
    if b==0:
        c=c+1
print(c)

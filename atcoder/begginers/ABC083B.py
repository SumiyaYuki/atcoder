n,a,b=map(int,input().split())
goukei=0
tmp=0
d=0
for i in range(1,n+1):
    c=0
    tmp=i
    for j in range(5):
        d=i-int(i/10)*10
        c=c+d
        i=(i-d)/10
    if a<=c<=b:
        goukei=goukei+tmp

print(goukei)

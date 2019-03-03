n,y=map(int,input().split())
a=-1
b=-1
c=-1

for i in range(0,n+1):
    for j in range(0,n-i+1):
        if 10000*i+5000*j+1000*(n-i-j)==y:
            a=i
            b=j
            c=n-i-j

print(str(a)+" "+str(b)+" "+str(c))

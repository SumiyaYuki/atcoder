a,b,k=map(int,input().split())
c=0
n=0
if a>b:
    n=a-b
if b>a:
    n=b-a
if a==b:
    n=a
while(True):
    if(a%n==0)&(b%n==0):
        c=c+1
    if c==k:
        break
    n=n-1
print(n)

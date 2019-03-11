n,m,c=map(int,input().split())
b=list(map(int,input().split()))
a=[]
d=0
count=0
for i in range(0,n):
    a.append(input().split())

for i in range(0,n):
    for j in range(0,m):
        d = d + int(a[i][j])*int(b[j])
    if d+c>0:
        count=count+1
    d=0

print(count)

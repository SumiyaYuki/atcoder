import copy
n=int(input())
s=list(input())
a=0
b=[]
count=0

while a<n:
    if s[a] not in b:
        b.append(s[a])
    if len(b)==27:
        break
    a=a+1
    
def search(retu,syurui,kaishi):
    c=copy.copy(syurui)
    d=copy.copy(retu)
    print(retu)
    global count
    count=count+1
    c.remove(kaishi)
    del d[:d.index(kaishi)]
    if len(c)==0:
        return 0
    for i in c:
        if i in d:
            search(d,c,i)

for i in b:
    search(s,b,i)

print(count%(10**9+7))

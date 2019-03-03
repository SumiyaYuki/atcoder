n=input()
d=[]
for i in range(int(n)):
    d.append(input())

e=[]
flag=0

for i in d:
    for j in e:
        if i==j:
            flag=1
    if flag==0:
        e.append(i)
    flag=0

print(len(e))

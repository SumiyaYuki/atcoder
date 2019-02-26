n=input()
a=list(map(int,input().split()))
alice=0
bob=0

def sort(list):
    temp=1
    while temp!=0:
        temp=0
        for i in range(len(list)-1):
            if (list[i]<list[i+1]):
                temp=list[i]
                list[i]=list[i+1]
                list[i+1]=temp
    return list

b=sort(a)

for i in range(len(b)):
    if (i-int(i/2)*2)==0:
        alice=alice+b[i]
    else:
        bob=bob+b[i]

print(alice-bob)

n,m,k = map(int,input().split())
matr =[]
item = [(int,int,[])]
ins = []
pos = 0
u=0
for i in range(n):
    ins = list(str(input()).split())
    j=0
    for x in range(0, len(ins), 3):
        e_c = ins[x : x + 3]
        item+=[(i,j,e_c)]
        j+=1
        e_c = ", ".join(e_c)
        matr.append(e_c) 
item.pop(0)
x = list(input().split())
while u!=k:
    print(item.index(x[u],pos))
    u+=1
print(item)
print(x)

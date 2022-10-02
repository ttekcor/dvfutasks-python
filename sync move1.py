inp = list(input())
x= int(inp[0])
lstx = list(map(int, input().split()))
lsty = list(map(int, input().split()))
i=0
lst=[]
while x>i:
    lst.append(lstx[i] * lsty[i])
    i+=1
res = [str(i) for i in lst]
print(res)
result=" ".join(res)
print(result)

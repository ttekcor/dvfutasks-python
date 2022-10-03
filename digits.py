fin = open('input.txt').readlines()
res=[]
for i in fin:
    if not i.isspace():
        res.append(i.replace('\n',''))

x = [1,2,3,4,5,6,7,8,9,0]
i = 0 
result = []
# res=set(res)
while i<len(x):
    if i in res:
        result.append((res.count(i)))
    else:
        pass
    i+=1
# for g,i in enumerate(res):
#     for r in res:
#         if i==r:
#             x[g]+=1

print(res)
print(result)
print(x)
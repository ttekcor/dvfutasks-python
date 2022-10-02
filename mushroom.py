x = int(input())
result = []
st=0
find = 'Boletus edulis'
while x>0:
    s = input()
    result.append(s)
    x-=1
for i in result:
    if find == i.capitalize():
        st+=1

print(st)
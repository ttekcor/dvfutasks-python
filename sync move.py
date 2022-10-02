x = int(input())
result = []
st=''
while x>0:
    s = input()
    result.append(s)
    x-=1
result.reverse()
st = "\n".join(result)

print(st)
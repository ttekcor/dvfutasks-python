x = input().split()
result = []
for i in x:
    tmp = abs(int(i))
    result.append(tmp)
print(sum(result))
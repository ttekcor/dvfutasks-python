from tokenize import Double


x = input().split()
result = []
for i in x:
    tmp = float(i)
    result.append(tmp**2)
result = sum(result)
sqrt = result ** (0.5)
print(sqrt)
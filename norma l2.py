x = input().split()
result = [(float(i)**2) for i in x]
# for i in x:
#     tmp = float(i)
#     result.append(tmp**2)
# result = sum(result)
sqrt = sum(result) ** (0.5)
print(sqrt)
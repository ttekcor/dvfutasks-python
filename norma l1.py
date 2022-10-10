# x = input().split()
# result = []
# for i in x:
#     tmp = abs(int(i))
#     result.append(tmp)
# print(sum(result))
x = input().split()
result = [(abs(int(i))) for i in x]
print(sum(result))
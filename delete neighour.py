# x = input().split()
# result = x.copy()[1:]
# for i in result:
#     if result.count('0'):
#         x.pop(result.index('0')-1)
#         result.remove("0")   
#     else: break
# print(" ".join(x))



data = list(map(int, input().split()))
data_index = [i for i in range(len(data))]
print(' '.join(map(str, map(lambda x: data[x], list(filter(lambda x: data[x + 1] != 0, data_index[:-1]))))), data[-1])
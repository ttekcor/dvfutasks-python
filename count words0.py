f1 = str(input())
text1 = [".",",","?","!"]
for i in f1:
    for x in text1:
        if x in f1:
            f1=f1.replace(x,"")
result = f1.split()
res_sum = len(result)
print(f1)
print(res_sum)

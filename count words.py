# f = open("/home/rockett/Desktop/input.txt" ) 
# text = [".",",","-","?","!","−"]
# result = []
# f1 = list(f.readline())
# f2=''
# for x in f1:
#     for i in text:
#         if i == x: 
#             f1.remove(x)
#             f1.append('|')
#     f2+=x
# result=f2.split("|")
# res_sum = len(result)
# print(result)
# print(f2)
# with open("/home/rockett/Desktop/output.txt","w") as wp:
#     wp.write(str(res_sum))
from cgitb import reset


f = open("/home/rockett/Desktop/input.txt" )
text = [".",",","!","?"]
sep = ""
result1=[]
f1 = list(f.readline())
for i in range(len(text)):
    for let in range(len(f1)):
        if text[i] in f1[let]:
            f1.pop(let)
            f1.insert(let,"|")
print(f1)

# f2=''
# for x in f1:
#     for i in text:
#         if i == x:
#             f2 = f1.replace(i,"|")
text = [".",",","!","-","?","|||\n"]
result="".join(f1)
result = result.split(" ")
for i in text:
    if i in result:
        result1=result.remove(i)
res_sum = len(result1)
print(f1)
print(result1)
print(res_sum)
with open("/home/rockett/Desktop/output.txt","w") as wp:
    wp.write(str(res_sum))
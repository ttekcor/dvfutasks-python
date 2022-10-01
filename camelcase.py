from unittest import result


fin = open('input.txt')
input_text = fin.readline()
result1=''
if input_text[0].isupper() == True:
    input_copy = []
    for i in input_text:
        if i.isupper() == True:
            tmp = i.lower()
            input_copy.append('_')
            input_copy.append(tmp) 
        elif(i.isupper()==False):
            input_copy.append(i)
    input_copy.pop(0)   
    res1 = result1.join(input_copy)
elif input_text[0].islower() == True:
    input_copy = input_text
    rec = input_copy.split("_")
    tmp = []
    for i in rec:
        tmp.append(i.capitalize())
        res1 = result1.join(tmp)
with open("/home/rockett/Desktop/output.txt","w") as wp:
    wp.write(str(res1))
# x='_'
# str2_result= []
# str_result = []
# res=''
# for i in input_text:
#     str2_result.append(i)
# for i in str2_result:
#     if x in str2_result:
#         input_copy.capitalize()
#         input_copy.split("_")
#         res1 = res.join(input_copy)
#         with open("/home/rockett/Desktop/output.txt","w") as wp:
#             wp.write (str(str2_result()))
#         print(1)

#     elif x not in input_text:
#         str_result = []
#         for i in input_text:
#             if i.isupper() == True:
#                 tmp = i.lower()
#                 str_result.append('_')
#                 str_result.append(tmp)
#             elif(i.isupper()==False):
#                 str_result.append(i)     
#         str_result.pop(0)   
#         res1 = res.join(str_result)
#         
#         print(2,str_result)
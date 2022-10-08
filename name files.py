with open('/home/rockett/Desktop/input.txt' , 'r') as f:
    a, *b = f.readlines()
    b = [x.rstrip('\n') for x in b]
    a = int(a)-1
b_copy = []
b_res = []
b_str =''
k=0
i = 0
b_copy.append(b[0])
while i<a:
    if b[i].lower() == b[i+1].lower():
        k+=1
        b_copy.append(b[i+1]+str(k))
    elif b[i].lower() != b[i+1].lower():
        k=0
        b_copy.append(b[i+1])
    else:
        break
    i+=1
for i in b_copy:
    for x in b_copy:
        if i!=x:
            if i.lower() == x.lower(): # проблема двойного вхождения!!!
                k+=1
                b_str=i+str(k)
        else:
            b_res.append(i)
b_res.append(b_str)
print(b_res)

with open ('/home/rockett/Desktop/output.txt' , 'w') as fout:
    print(str(b_copy),file=fout,end="")

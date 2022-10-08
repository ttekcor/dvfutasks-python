with open('/home/rockett/Desktop/input.txt' , 'r') as f:
    f1 = f.readlines()
result=[]
f1 = str(f1[0])
f1=f1.replace('?',' ')
f1=f1.replace('!',' ')
f1=f1.replace('.',' ')
f1=f1.replace(',',' ')
f1=f1.replace('\n',' ')
f1 = f1.replace(' - ', ' ')
result = f1.split()
res_sum = len(result)
with open ('/home/rockett/Desktop/output.txt' , 'w') as fout:
    print(str(res_sum),file=fout,end="")

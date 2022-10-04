x = int(input())
matr=[]
for i in range(x):
    ins = list(str(input()).split())
    matr.append(ins)  
y=list(zip(*matr))
for i in y:
        matr_in=''
        for j in i:
            matr_in=matr_in+j+' '
        print(matr_in)
print(y)
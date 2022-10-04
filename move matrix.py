m,n,k = map(int,input().split())
matr =[]
for i in range(m):
    ins = list(str(input()).split())
    matr.append(ins)  
if k%4==0:
    for i in matr:
        matr_in=''
        for j in i:
            matr_in=matr_in+j+' '
        print(matr_in)
elif k%4==1:
    y = list(zip(*matr[::-1]))
    for i in y:
        matr_in=''
        for j in i:
            matr_in=matr_in+j+' '
        print(matr_in)
elif k%4==2:
    y1= zip(*reversed(list(zip(*matr[::-1]))))
    for i in y1:
        matr_in=''
        for j in i:
            matr_in=matr_in+j+' '
        print(matr_in)
elif k%4==3:
    y1= reversed(list(zip(*matr[::+1])))
    for i in y1:
        matr_in=''
        for j in i:
            matr_in=matr_in+j+' '
        print(matr_in)

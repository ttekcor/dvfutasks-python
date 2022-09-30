x = int(input())
y = [1,2,3,4,5,6,7,8,9,10,11]
u=1
if(100>=x>=1):
    del y[x:len(y)]
    while u<=x:
        for i in y:
            res = i*u
            print(u,'*',i,'=',res)
        u+=1
#таблица умножения
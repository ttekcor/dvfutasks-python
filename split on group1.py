x = str(input())
result = []
st1=[]
st2=[]
i=0
s=0
result.append(x)
while s!=5:
    y = str(input())
    if y!='':
        result.append(y)
    elif y=="":
        break
    s+=1
for x in result:
    if(i%2==0):
        st1.append(x)
    elif(i%2!=0):
        st2.append(x)
    i+=1
st1=", ".join(st1)
st2=", ".join(st2)
print(result)
print(st1)
print(st2)
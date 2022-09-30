fin = open ( "/home/rockett/Desktop/input.txt" ) 
str1 = fin.readline().split()
a, b, t = int(str1[0]), int(str1[1]), int(str1[2])
z = a+b
otr =(2*z)
x = 2*a+b
tmp = []
if(t>=otr):
    t = t%otr
# for i in range(otr):
#     tmp.append(i)
if(a>t):
    re = 'S'
elif(a<=t<(z)):
    re = 'E'
elif((z)<=t<(x)):
    re = 'N'
elif((x)<=t<(otr)):
    re = 'W'
with open("/home/rockett/Desktop/output.txt","w") as wp:
    wp.write(str(re))
 
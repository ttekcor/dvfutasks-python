#f=open('/home/rockett/Desktop/input.txt')

def find_center(a, b):
    x = min(a,b)
    y = max(a,b)

    if not can_exist(a,b): return False

    while x:
        x-=1
        y+=1
        
        if x == y: return 0
    else:
        return y -1

def can_exist(a,b):
    x = min(a,b)
    y = max(a,b)

    while x+1 != y:
        x+=1
        y-=1
        
        if x == y: return False
    return True

fin = open("/home/rockett/Desktop/input.txt" ) 
st1 = fin.readline().split()
a, b = int(st1[0]), int(st1[1])
x=min(a,b)
y=max(a,b)

with open("/home/rockett/Desktop/output.txt","w") as wp:
   wp.write(str(find_center(x,y)))
   # print(2%4)
# if((x+y-1)%2!=0 or (x+y-1)%4!=0):
#    p = 0

# elif(x<y and x>=1 and y<=1000000):
#    p = ((x-1)+y)/2
   
#    #while x!=1:
#       #x=x-1
#       #y=y+1
#       #print(x,y)
#       #if(x%2!=0):
         
   
# else:
#    p = 0 
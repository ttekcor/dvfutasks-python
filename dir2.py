x =input()
arr=[]
list(arr.append(i) for i in dir(eval(x)) if "__" not in i)
list(arr.append(i) for i in dir(eval(x)) if "__" in i)
for i in arr:
    print (i)

arr=[]
list(arr.append(i) for i in sorted(str.__dict__.keys()) if "__" not in i)
list(arr.append(i) for i in sorted(str.__dict__.keys()) if "__" in i)
for i in arr:
    print (i,"\n")

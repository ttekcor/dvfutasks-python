x,y = input().split()
lst = list(map(int,input().split()))
lst_pos = list(map(int,input().split()))
lst.insert(0,0)
result = list(map(int,lst))
res = list(i for i in lst if lst_pos.count(i))
# for i in lst_pos:
#         result[i]=result[i]+1
        
print(res)
# a = list(map(int,map(lambda i:lst_pos.count(lst[i]),range(int(x))))) 
# print(a)
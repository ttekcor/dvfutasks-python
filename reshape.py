x,lst = input(),input().split()
n,m = input().split()

a = ([lst[i:i + int(m)] for i in range(0, len(lst), int(m) )])
for i in a:
    res = " ".join(i)
    print(res)



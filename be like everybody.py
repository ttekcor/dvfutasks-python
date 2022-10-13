x = input().split()
x_min = min(x, key=int)
x_max = max(x, key=int)
print(" ".join([x_min if i == x_max else i for i in x]))


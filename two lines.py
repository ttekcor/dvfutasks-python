x = input().split()
print(' '.join(x[:2]+x[2:(len(x)-2)][::-1]+x[(len(x)-2):]))
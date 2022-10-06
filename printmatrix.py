def PrintMatrix(a):
    output = [list(str(x).split(',')) for x in a]
    print('\n'.join(map(' '.join,map(lambda x: map(str, x),a))))
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
PrintMatrix(mat)

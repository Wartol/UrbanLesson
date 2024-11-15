def get_matrix(n,m,value):
    matrix = []
    for strok in range(n):
        matrix.append([value])
        for stolb in range(m):
            matrix[strok].append(value)
    return matrix
print(get_matrix(2,3,10))
print(get_matrix(3,4,50))
print(get_matrix(4,5,100))
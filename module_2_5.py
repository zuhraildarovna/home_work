def get_matrix (n, m, value):
     matrix = []
     for i in range (0, n):
         mat_1 = []
         for j in range (0,m):
             mat_1.append(value)
         matrix.append(mat_1)
     return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)




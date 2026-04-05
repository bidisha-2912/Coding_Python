A = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = []
for i in range(3):  
    row = []
    for j in range(2):  
        row.append(A[j][i])
    transpose.append(row)
print("Transpose Matrix:")
for row in transpose:
    print(row)

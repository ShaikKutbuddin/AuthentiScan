# Matrices
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

# --------------------
# Matrix Addition
# --------------------
rows = len(A)
cols = len(A[0])
add_result = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    add_result.append(row)

# --------------------
# Matrix Transpose (of A)
# --------------------
transpose_result = []
for j in range(cols):
    row = []
    for i in range(rows):
        row.append(A[i][j])
    transpose_result.append(row)

# --------------------
# Matrix Multiplication
# --------------------
mul_result = []
for i in range(len(A)):
    row = []
    for j in range(len(B[0])):
        s = 0
        for k in range(len(B)):
            s += A[i][k] * B[k][j]
        row.append(s)
    mul_result.append(row)

# --------------------
# Print Results
# --------------------
print("Matrix A:")
for r in A:
    print(r)

print("\nMatrix B:")
for r in B:
    print(r)

print("\nMatrix Addition (A + B):")
for r in add_result:
    print(r)

print("\nMatrix Transpose of A:")
for r in transpose_result:
    print(r)

print("\nMatrix Multiplication (A * B):")
for r in mul_result:
    print(r)
# -------------------------
  # Output
# ------------------------------
""""
Matrix A:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Matrix B:
[9, 8, 7]
[6, 5, 4]
[3, 2, 1]

Matrix Addition (A + B):
[10, 10, 10]
[10, 10, 10]
[10, 10, 10]

Matrix Transpose of A:
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]

Matrix Multiplication (A * B):
[30, 24, 18]
[84, 69, 54]
[138, 114, 90]
"""

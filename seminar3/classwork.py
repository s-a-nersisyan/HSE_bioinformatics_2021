a = [1, 3, 2, 6, 4, 5]
S = [0] * len(a)

S[0] = a[0]
S[1] = a[1]

for i in range(2, len(S)):
    S[i] = min(S[i - 1], S[i - 2]) + a[i]

print(a)
print(S)

matrix = [[1, 5, 6], [-123, 0, 11]]
print(matrix[1][2])
matrix[1][2] = 100500
print(matrix[1][2])

m, n = 5, 3
matrix = []
for i in range(m):
    zero_row = [0] * n
    matrix.append(zero_row)

print(matrix)

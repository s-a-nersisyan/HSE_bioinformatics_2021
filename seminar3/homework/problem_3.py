'''
Задача номер 3
'''
a = [1, 2, 100, 3, 1000, 1]

S = [0] * len(a)
S[0] = a[0]
S[1] = a[1]
for i in range(2, len(S)):
    S[i] = min(S[i - 1], S[i - 2]) + a[i]

inverse_path = []
i = len(S)
while i >= 0:
    if i == 0:
        inverse_path.append(1)
        break
    if i == 1:
        inverse_path.append(2)
        break

    if S[i - 1] < S[i - 2]:
        inverse_path.append(1)
        i -= 1
    else:
        inverse_path.append(2)
        i -= 2

path = inverse_path[::-1]
print(a)
print(S)
print(path)

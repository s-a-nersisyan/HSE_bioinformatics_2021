# Maximal sum of sub-array
x = [1, 2, -10, 9, 1]

S = [0] * len(x)
S[0] = x[0]
for i in range(1, len(S)):
    S[i] = max(S[i - 1] + x[i], x[i])

print(S)

# What is dict
a = {"Petya": 21, "Ivan": 49, "Anna": 17}
print(a["Anna"])
a["Inna"] = 99
print(a)

# Dict keys can be explicitly hashed
print(hash("Petya"))
print(hash("Anna"))


# Example of dict usage: count number of occurences of each symbol in a string
s = "hello world i am superman!"
counts = {}
for symbol in s:
    counts[symbol] = counts.get(symbol, 0) + 1

print(counts)


# How to read SARS-CoV-2 genome from fasta file
f = open("homework/SARS-CoV-2.fasta")
f.readline().strip()
genome = f.readline().strip()
print(genome)

# Sets
A = {1, 3, 5, 7, 9, "qwerty"}
B = {3, 9, "qwerty", "uiop"}
print(A)
print(B)
print(A.intersection(B))
print(A.union(B))
print(A.difference(B))

a = [1, 4, 1, 5, 6, 7]
print(sorted(list(set(a))))

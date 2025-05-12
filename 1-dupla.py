from itertools import combinations

nomes = ["Ana", "Bia", "Davi", "Bruno"]

duplas = list(combinations(nomes, 2))

for dupla in duplas:
    print(dupla)
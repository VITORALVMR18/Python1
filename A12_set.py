#Set (conjunto)
# conjunto1 = {1, 2, 3, 4, 5, 6, 5, 4}
# set não considera as repetições

conjunto = {1, 2, 3, 4, 5, 4, 5, 4}
print(conjunto)

nomes = {"vitor", "tadeu", "abrahao", "tadeu", "vitor"}
print(nomes)

conjunto.add(9)
conjunto.remove(3)
print(conjunto)

outroConjunto = {7, 5, 3, 9, 1}
uniao = conjunto.union(outroConjunto)
print()
print(uniao)

diferença = conjunto.difference(outroConjunto)
print(diferença)

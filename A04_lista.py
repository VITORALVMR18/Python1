# lista = conjunto de valores
# lista = [valor 1, valor2, ...]
# lista = list(valor 1, valor 2, ...)

listaVazia = [] # cria lista vazia

listaComElementos = [1, 2, 3, 4, 5, 6, 7,]
listaComElementosMista = [7, "Python", 3.14159, True, 'c']

listaComElementos[0] # pega o primeiro elemento]
listaComElementos[-1] # pega o ultimo elemento
listaComElementos[:4] # pega os 3 primeiros elementos 
listaComElementos[3:] # pega do terceiro item em diante
listaComElementos[3:5] # pega do terceiro até o quinto
listaComElementos[3:8:2] # pega do terceiro  ao sétimo de 2 em 2

print(listaComElementos[3:8:2])

len(listaComElementos[3:8:2])

len(listaComElementos) # retorna numero de elementos
print(len(listaComElementos))

max(listaComElementos) # retorna o maior valor
print(max(listaComElementos))

min(listaComElementos) # retorna o menor valor
sum(listaComElementos) # retorna todas as somas de todos os elementos

print(sum(listaComElementos))
sorted(listaComElementos) # retorna a lista em ordem crescente

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

listaVazia.append(1) # adiciona um elemento 
listaVazia.append("Texto")
listaVazia.append(True)

listaVazia.insert(2, "Novo elemento") #adiciona elemento no indicie 2
print(listaVazia)

listaVazia.remove("Texto") # remove o primeiro elemento encontrado
print(listaVazia)

print(listaVazia.pop(0))
print(listaVazia)

print(listaVazia.index("Novo elemento"))

listaNacoes = ["Brasil", "Eua", "China", "Canada", "Inglaterra"]

print(listaNacoes.count("Eua"))

novalista = listaNacoes.copy()
print(novalista)

temElemento = "canada" in novalista
print(temElemento)

while True:
    if "Brasil" in listaNacoes
    print("Descobri o Brasil")
    listaNacoes.remove("Brasil")
elif "Inglaterra" in listaNacoes:
# TUPLA
# tupla = (elemento1, elemento2, ...)

variavel1 = 9 # variavel tipo numerica
variavel2 = "Texto" # variavel tipo string
variavel3 = True # variavel tipo boleano
variavel4 = ["Item1", "Item2", "Item3"] # lista
variavel5 = ("Item1", "Item2", "...") # tupla

tupla = (1, "Olá", 3,14, True 'c') # é imutavel
tuplaDireita = 0, "Edson", 1.618, 'p', "Edson"
tuplaVazia = ()
tuplaSimples = (27,)

print(tupla[1])
print(tupla[3])

print[]
for indice, elemento in enumerate(tupla):
    print(f"{indice}: {elemento}")

tuplaAlinhada = ((1,2,3), 1, True,[1, 4, "sin"])
print()
print(tuplaAlinhada[0])
print(tuplaAlinhada[1])
print(tuplaAlinhada[3][2])
print(len(tuplaDireita))
print(tupla.index(3,14))
print(tuplaDireita.count("Edson"))

string = "Curso"
print(tupla(string))

novaTupla = tupla(string)
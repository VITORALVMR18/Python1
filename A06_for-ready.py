# laço de repetição "for" e range

listaNacoes = ["Brasil", "Eua", "China", "Canada", "Inglaterra"]

for país in listaNacoes:
    print(país)

for caracter in "Ciencia de Dados":
    print(caracter)

meninas = [["Amelia", "Ana Paula", "Alice"], ["Beatriz", "Bianca", "Berenice"], ["Sofia", "Sandra",]]
for menina in meninas:
    print(menina)
    for nome in menina:
        print(nome)

# Range:
for i in range(5):
    print(i)

for i in range(2, 9):
    print(i)

for i in range(5, 17, 2):
    print(i)
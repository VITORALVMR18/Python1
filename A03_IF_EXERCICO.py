# faça umma rotina com o uso de if, elif, else  quer receba um valor numerico inteiro entre 1 e 100 e print se a pessoa com a idade obrigatoria

acordei = True
if acordei:
    print("acordei cedo")
else:
    print("faltei na escola")

if acordei:
    print("me arrumei e fui ao colegio")
else:
    print("Não fui ao colegio e tomei esporro")

idade = int(input("Digite a idade: "))
if idade >= 60:
    print("voto opcional")
elif idade >= 18:
    print("voto obrigatório")
elif idade >= 16:
    print("voto opcional")
else:
    print("Não pode votar também")

print("Terminado")

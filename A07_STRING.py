#string = "hello world"
#for caracter in string:
    #print(caracter)

    #print(string[6])
    #print(string[7:12])
    #print("Olá, Mundo"[5:10])
    #print("Bom dia"[-1])

s1 = "Vamos"
s2 = "Ja!"
print(s1 +" "+ s2)
texto = (len("Tamanho de um texto. "))

mensagem = "Tudo que é solido se desmancha no ar."
print("lid" in mensagem) # True
print("y" in mensagem) # False

# Fatiamento
slicing = mensagem[11:17]
print(slicing) # "é solido"

print(mensagem.upper())
print(mensagem.lower())
print(mensagem.replace("o ar", "a atmosfera"))
print(" Hoje em dia.".replace(" ", ""))
# DICIONARIO
# dicionario = {chave:valor}
# dicionario = dint(chave:valor)

dicionario = {}

dicionario["Cidade"] = "SP"
dicionario["Estado"] = "São Paulo"
dicionario["Região"] = "Sudeste"

print(dicionario)
print(dicionario["Cidade"])
print(dicionario.get("Estado"))
print(dicionario.get("ChaveInexistente"))
print(dicionario.get("ChaveInexistente", "Valor alternativo se chave não existir"))

frutas = {
    "Laranja: R$5,00",
    "Pera: R$3,00"
}
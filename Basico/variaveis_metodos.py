frutas = ["pera", "limão", "abacate"]

# pessoas = ["Jose", "Pedro", "Ana"]

# print (frutas)
# print (pessoas)

frutas.append("laranja")
frutas.insert(2, "uva")
frutas.remove("limão")
print(frutas)

elemento = frutas.pop(2)
print(elemento)
print(frutas)

# frutas.reverse()
# print(frutas)

frutas.sort()
print(frutas)

frutas.append("uva")
frutas.append("uva")
print(frutas)

num_uvas = frutas.count("uva")
print("A quantidade de uvas apareceu", num_uvas)

cadastro = {
    "nome":         "Jairo",
    "sobrenome":    "Candido",
    "idade":         90,
    "endereço":      "Rua Luis Lacava",
    "cidade":        "Mauá",
    "estado":        "São Paulo"
}

print(cadastro.keys())
print(cadastro.values())

nome = cadastro.get("nome")
print(nome)
print(cadastro)
cadastro.clear()

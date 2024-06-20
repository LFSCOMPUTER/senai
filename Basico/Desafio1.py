# Desafio 1 - Calculo IMC

# text
nome = input("Olá, qual é seu nome:")
# Número Real
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura:"))

# round > arrendondamento
imc = peso / (altura ** 2)
imc = round(imc, 2)

print(f" {nome} seu IMC é {imc}")

# ----------> Desafio 9
# Fazer um programa para o usuario digitar 2 numeros sendo o 
# primeiro menor que o segundo e mostrar os numeros pares 
# entre esses 2 numeros
# Dica: utilizar o operador de resto - % - para descobrir
# se o numero é par

numero1 = int(input("digite o 1° numero: "))
numero2 = int(input("digite o 2° numero: "))

while num1 <=numero2:
    if (num1 % 2) == 0:
        print(num1)

for i in range(numero1, numero2 + 1):
    if i % 2 == 0:
        print(i)
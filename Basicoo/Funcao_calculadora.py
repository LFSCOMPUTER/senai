# Exercicio Funções
#Criar as funções main() e as demais funções para criar uma
# calculadora com operações +,-, /, *.
# As funções devera realizar somente o calculo
# O usuario devera digitar 2 numeros e a operação que deseja realizar
# OBS.: seu codigo devera bloquear a divisao por zero

# Criar as funçoes para o calculo



def adicao(a, b):
    return a + b


def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b


def main():

    print('Oá, bem vindo a Calculadora SENAI')
    num1 = int (input('Digite o primeiro numero para calculo '))
    num2 = int (input('Digite o segundo numero para calculo '))
    operacao = input("Digite a operacao a ser calculado ")
    
    if operacao == "+":
        resultado = adicao(num1, num2)
        print("O resultado da adição é:", resultado)
    elif operacao == "-":
        resultado = subtracao(num1, num2)
        print("O resultado da subtração é:", resultado)
    elif operacao == "*":
        resultado = multiplicacao(num1, num2)
        print("O resultado da multiplicação é:", resultado)
    elif operacao == "/":
        resultado = divisao(num1, num2)
        print("O resultado da divisão é:", resultado)

    else:
        print("Não existe divisao por zero!")

    else:
        print("Operação inválida!")




if __name__ =="__main__":
    main()


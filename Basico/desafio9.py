# Programa de Calculadora:
# - O programa deverá receber 2 numeros reais do usuario;
# - O programa deverá receber a operação matemática para ser executada,
# as operações podem ser +, -, /, *
# - Os cálculos devem ser realizados por funções
# - Informar o resultado final para o usuário

def soma(num1,num2):
    res = num1 + num2
    return res

def subtracao(num1,num2):
    res = num1 - num2
    return res

def divisao(num1,num2):
    res = num1 / num2
    return res

def multiplicacao(num1,num2):
    res = num1 * num2
    return res    

def main():
    num1 = float(input("Digite um numero para calculo:"))
    num2 = float(input("Digite outro numero para calculo:"))

    operacao = input("Digite a operação a ser realizada(+, -, /, *):")

    if operacao == '+':
        res = soma(num1, num2)
        print("O resultado da operacao eh:", res)
    elif operacao == '-':
        res = subtracao(num1, num2)
        print("O resultado da operacao eh:", res)
    elif operacao == '/':
        if num2 != 0:
            res = divisao(num1, num2)
            print("O resultado da operacao eh:", res)
        else:
            print("Não existe divisão por zero!!!")
        res = divisao(num1, num2)
        print("O resultado da operacao eh:", res)
    elif operacao == '*':
        res = multiplicacao(num1, num2)
        print("O resultado da operacao eh:", res)
    else:
        print("Se nenhuma operação for digitada o programa não ira proseguir")

if __name__ == "__main__":
    main()
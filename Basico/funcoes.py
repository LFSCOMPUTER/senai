#  Funções (definição simplória):
# - Parte do código que eu quero que aconteça varias vezes
# - Módulo separado do módulo principal

#FUNÇAO CALCULAR IMC
def calcularIMC(peso,altura):
    imc = peso / (altura ** 2)
    imc = round(imc, 2)

#FUNÇAO PRINCIPAL
def main():
    nome = input("Olá, qual é seu nome:")

    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura:"))

    imc = calcularIMC(peso,altura)

    print(f" {nome} seu IMC é {imc}")



# CONDIÇAO PARA EXECUTAR A FUNÇAO PRINCIPAL
if __name__ == "__main__":
    main()



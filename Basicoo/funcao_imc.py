#Modulo calculo do imc
def calcularIMC(altura, peso):

    imc = peso /(altura  ** 2)

    return imc

# Modulo de  mensagem ao usuario do IMc
def imprimirIMC(imc):

    print(f"Ola usuario, seu Imc é {imc}!!!")

# Modulo Mensagem de boas vindas
def imprimirBoasVindas():

    print('********* SISTEMA DE CALCULO DO IMC *******')
    print("Oça, seja bem vindo ao sitema de calculo do IMC")

# Módulo Principal

def main():

    imprimirBoasVindas()

    resultado = calcularIMC(1.80, 88)
    resultado = round (resultado,2)

    imprimirIMC(resultado)

if __name__== "__main__":
    main()

